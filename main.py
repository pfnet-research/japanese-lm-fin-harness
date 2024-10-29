import argparse
import json
import logging
import os
import sys
from typing import Union

import numpy as np
from lm_eval import evaluator
from lm_eval import utils
from lm_eval.__main__ import parse_eval_args
from lm_eval.__main__ import setup_parser
from lm_eval.api.task import ConfigurableTask
from lm_eval.evaluator import request_caching_arg_to_dict
from lm_eval.loggers import EvaluationTracker
from lm_eval.loggers import WandbLogger
from lm_eval.utils import handle_non_serializable
from lm_eval.utils import make_table
from lm_eval.utils import simple_parse_args_string

from jlm_fin_eval.tasks import TaskManager

ConfigurableTask.original_process_results = ConfigurableTask.process_results

eval_logger = logging.getLogger("lm-eval")


def process_results(self: ConfigurableTask, doc: dict, results: dict) -> dict:
    result_dict = self.original_process_results(doc, results)
    use_metric = list(self._metric_fn_list.keys())
    metrics = list(set(use_metric) - set(result_dict.keys()))
    if len(metrics) > 0:
        if self.OUTPUT_TYPE == "multiple_choice":
            lls, is_greedy = zip(*results)
            choices = self.doc_to_choice(doc)
            completion_len = np.array([float(len(i)) for i in choices])

            pred = np.argmax(lls)
            pred_norm = np.argmax(lls / completion_len)

            if self.multiple_input:
                gold = self.doc_to_text(doc)
            else:
                gold = self.doc_to_target(doc)

            gold_index_error = False
            if isinstance(gold, list):
                gold = [i if i < len(choices) else -100 for i in gold]
                if -100 in gold:
                    gold_index_error = True
            else:
                if isinstance(gold, int):
                    gold = gold if gold < len(choices) else -100
                elif isinstance(gold, str):
                    gold = choices.index(gold) if gold in choices else -100

                if gold == -100:
                    gold_index_error = True

            if gold_index_error:
                eval_logger.warning(
                    f"Label index was not in within range of available choices,"
                    f"Sample:\n\n{doc}\n\n"
                )

            if self.multiple_target:
                acc = 1.0 if pred in gold else 0.0
                acc_norm = 1.0 if pred_norm in gold else 0.0
                exact_match = int(any([is_greedy[i] if i != -100 else 0 for i in gold]))
            else:
                acc = 1.0 if pred == gold else 0.0
                acc_norm = 1.0 if pred_norm == gold else 0.0
                # TODO: this gets score of 0 on arc_challenge for pythia-70m. need to test that this works properly
                exact_match = int(is_greedy[gold]) if gold != -100 else 0

            if (
                len(
                    set(
                        [
                            "map",
                            "map_2",
                            "map_3",
                            "map_4",
                            "map_norm",
                            "map_2_norm",
                            "map_3_norm",
                            "map_4_norm",
                        ]
                    )
                    & set(use_metric)
                )
                != 0
            ):
                ranking = np.argsort(lls)[::-1].tolist()
                ranking_norm = np.argsort(lls / completion_len)[::-1].tolist()
                correct_answer_ranking = ranking.index(gold) + 1
                correct_answer_ranking_norm = ranking_norm.index(gold) + 1
                map_score = 1.0 / correct_answer_ranking
                map_2 = 0.0 if correct_answer_ranking > 2 else map_score
                map_3 = 0.0 if correct_answer_ranking > 3 else map_score
                map_4 = 0.0 if correct_answer_ranking > 4 else map_score
                map_score_norm = 1.0 / correct_answer_ranking_norm
                map_2_norm = 0.0 if correct_answer_ranking_norm > 2 else map_score_norm
                map_3_norm = 0.0 if correct_answer_ranking_norm > 3 else map_score_norm
                map_4_norm = 0.0 if correct_answer_ranking_norm > 4 else map_score_norm

            result_dict.update(
                {
                    **(
                        {"f1_norm": (gold, pred_norm)}
                        if "f1_norm" in use_metric
                        else {}
                    ),
                    **({"map": map_score} if "map" in use_metric else {}),
                    **({"map_2": map_2} if "map_2" in use_metric else {}),
                    **({"map_3": map_3} if "map_3" in use_metric else {}),
                    **({"map_4": map_4} if "map_4" in use_metric else {}),
                    **(
                        {"map_norm": map_score_norm} if "map_norm" in use_metric else {}
                    ),
                    **(
                        {"map_2_norm": map_2_norm} if "map_2_norm" in use_metric else {}
                    ),
                    **(
                        {"map_3_norm": map_3_norm} if "map_3_norm" in use_metric else {}
                    ),
                    **(
                        {"map_4_norm": map_4_norm} if "map_4_norm" in use_metric else {}
                    ),
                }
            )
        else:
            raise NotImplementedError

    return result_dict


ConfigurableTask.process_results = process_results


def cli_evaluate(args: Union[argparse.Namespace, None] = None) -> None:
    if not args:
        # we allow for args to be passed externally, else we parse them ourselves
        parser = setup_parser()
        args = parse_eval_args(parser)

    if args.wandb_args:
        wandb_logger = WandbLogger(**simple_parse_args_string(args.wandb_args))

    eval_logger = utils.eval_logger
    eval_logger.setLevel(getattr(logging, f"{args.verbosity}"))
    eval_logger.info(f"Verbosity set to {args.verbosity}")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # update the evaluation tracker args with the output path and the HF token
    if args.output_path:
        args.hf_hub_log_args += f",output_path={args.output_path}"
    if os.environ.get("HF_TOKEN", None):
        args.hf_hub_log_args += f",token={os.environ.get('HF_TOKEN')}"
    evaluation_tracker_args = simple_parse_args_string(args.hf_hub_log_args)
    evaluation_tracker = EvaluationTracker(**evaluation_tracker_args)

    if args.predict_only:
        args.log_samples = True
    if (args.log_samples or args.predict_only) and not args.output_path:
        raise ValueError(
            "Specify --output_path if providing --log_samples or --predict_only"
        )

    if args.fewshot_as_multiturn and args.apply_chat_template is False:
        raise ValueError(
            "When `fewshot_as_multiturn` is selected, `apply_chat_template` must be set (either to `True` or to the chosen template name)."
        )

    if args.include_path is not None:
        eval_logger.info(f"Including path: {args.include_path}")
    task_manager = TaskManager(args.verbosity, include_path=args.include_path)

    if "push_samples_to_hub" in evaluation_tracker_args and not args.log_samples:
        eval_logger.warning(
            "Pushing samples to the Hub requires --log_samples to be set. Samples will not be pushed to the Hub."
        )

    if args.limit:
        eval_logger.warning(
            " --limit SHOULD ONLY BE USED FOR TESTING."
            "REAL METRICS SHOULD NOT BE COMPUTED USING LIMIT."
        )

    if args.tasks is None:
        eval_logger.error("Need to specify task to evaluate.")
        sys.exit()
    elif args.tasks == "list":
        print(task_manager.list_all_tasks())
        sys.exit()
    elif args.tasks == "list_groups":
        print(task_manager.list_all_tasks(list_subtasks=False, list_tags=False))
        sys.exit()
    elif args.tasks == "list_tags":
        print(task_manager.list_all_tasks(list_groups=False, list_subtasks=False))
        sys.exit()
    elif args.tasks == "list_subtasks":
        print(task_manager.list_all_tasks(list_groups=False, list_tags=False))
        sys.exit()
    else:
        if os.path.isdir(args.tasks):
            import glob

            task_names = []
            yaml_path = os.path.join(args.tasks, "*.yaml")
            for yaml_file in glob.glob(yaml_path):
                config = utils.load_yaml_config(yaml_file)
                task_names.append(config)
        else:
            task_list = args.tasks.split(",")
            task_names = task_manager.match_tasks(task_list)
            for task in [task for task in task_list if task not in task_names]:
                if os.path.isfile(task):
                    config = utils.load_yaml_config(task)
                    task_names.append(config)
            task_missing = [
                task for task in task_list if task not in task_names and "*" not in task
            ]  # we don't want errors if a wildcard ("*") task name was used

            if task_missing:
                missing = ", ".join(task_missing)
                eval_logger.error(
                    f"Tasks were not found: {missing}\n"
                    f"{utils.SPACING}Try `lm-eval --tasks list` for list of available tasks",
                )
                raise ValueError(
                    f"Tasks not found: {missing}. Try `lm-eval --tasks {{list_groups,list_subtasks,list_tags,list}}` to list out all available names for task groupings; only (sub)tasks; tags; or all of the above, or pass '--verbosity DEBUG' to troubleshoot task registration issues."
                )

    import datasets

    datasets.config.HF_DATASETS_TRUST_REMOTE_CODE = True

    eval_logger.info(f"Selected Tasks: {task_names}")

    request_caching_args = request_caching_arg_to_dict(
        cache_requests=args.cache_requests
    )

    results = evaluator.simple_evaluate(
        model=args.model,
        model_args=args.model_args,
        tasks=task_names,
        num_fewshot=args.num_fewshot,
        batch_size=args.batch_size,
        max_batch_size=args.max_batch_size,
        device=args.device,
        use_cache=args.use_cache,
        limit=args.limit,
        check_integrity=args.check_integrity,
        write_out=args.write_out,
        log_samples=args.log_samples,
        evaluation_tracker=evaluation_tracker,
        system_instruction=args.system_instruction,
        apply_chat_template=args.apply_chat_template,
        fewshot_as_multiturn=args.fewshot_as_multiturn,
        gen_kwargs=args.gen_kwargs,
        task_manager=task_manager,
        verbosity=args.verbosity,
        predict_only=args.predict_only,
        random_seed=args.seed[0],
        numpy_random_seed=args.seed[1],
        torch_random_seed=args.seed[2],
        fewshot_random_seed=args.seed[3],
        **request_caching_args,
    )

    if results is not None:
        if args.log_samples:
            samples = results.pop("samples")
        dumped = json.dumps(
            results, indent=2, default=handle_non_serializable, ensure_ascii=False
        )
        if args.show_config:
            print(dumped)

        batch_sizes = ",".join(map(str, results["config"]["batch_sizes"]))

        # Add W&B logging
        if args.wandb_args:
            try:
                wandb_logger.post_init(results)
                wandb_logger.log_eval_result()
                if args.log_samples:
                    wandb_logger.log_eval_samples(samples)
            except Exception as e:
                eval_logger.info(f"Logging to Weights and Biases failed due to {e}")

        evaluation_tracker.save_results_aggregated(
            results=results, samples=samples if args.log_samples else None
        )

        if args.log_samples:
            for task_name, config in results["configs"].items():
                evaluation_tracker.save_results_samples(
                    task_name=task_name, samples=samples[task_name]
                )

        if (
            evaluation_tracker.push_results_to_hub
            or evaluation_tracker.push_samples_to_hub
        ):
            evaluation_tracker.recreate_metadata_card()

        print(
            f"{args.model} ({args.model_args}), gen_kwargs: ({args.gen_kwargs}), limit: {args.limit}, num_fewshot: {args.num_fewshot}, "
            f"batch_size: {args.batch_size}{f' ({batch_sizes})' if batch_sizes else ''}"
        )
        print(make_table(results))
        if "groups" in results:
            print(make_table(results, "groups"))

        if args.wandb_args:
            # Tear down wandb run once all the logging is done.
            wandb_logger.run.finish()


if __name__ == "__main__":
    cli_evaluate()
