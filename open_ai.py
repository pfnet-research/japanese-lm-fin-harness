import argparse
import collections
import json
import os
import random
import re
import time
from typing import Any
from typing import Dict
from typing import Iterator
from typing import cast

import lm_eval.evaluator
import openai
from tqdm import tqdm

import jlm_fin_eval.tasks
from main import MultiChoice
from main import pattern_match

openai.api_type = os.environ.get("OPENAI_API_TYPE", "open_ai")
openai.api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
openai.api_version = os.environ.get("OPENAI_API_VERSION")
openai.api_key = os.environ.get("OPENAI_API_SECRET_KEY")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str)
    parser.add_argument(
        "--tasks",
        default=None,
        choices=cast(Iterator[str], MultiChoice(jlm_fin_eval.tasks.ALL_TASKS)),
    )
    parser.add_argument("--num_fewshot", type=int, default=0)
    parser.add_argument("--output_path", default=None)

    return parser.parse_args()


def oa_chat_completion(**kwargs: Any) -> Dict:
    """Query OpenAI API for completion.

    Retry with back-off until they respond
    """
    import openai

    backoff_time = 3.0
    while True:
        try:
            return openai.ChatCompletion.create(**kwargs)  # type: ignore
        except openai.OpenAIError:
            import traceback

            traceback.print_exc()
            time.sleep(backoff_time)
            backoff_time *= 1.5


def main() -> None:
    args = parse_args()

    if args.tasks is None:
        task_names = jlm_fin_eval.tasks.ALL_TASKS
    else:
        task_names = pattern_match(args.tasks.split(","), jlm_fin_eval.tasks.ALL_TASKS)
    print(f"Selected model: {args.model}")
    print(f"Selected Tasks: {task_names}")

    tasks = task_names
    num_fewshot = args.num_fewshot
    engine = args.model
    output_path = args.output_path

    task_dict = jlm_fin_eval.tasks.get_task_dict(tasks)  # type: ignore

    task_dict_items = [
        (name, task)
        for name, task in task_dict.items()
        if (task.has_validation_docs() or task.has_test_docs())
    ]
    versions: Dict[str, str] = {}

    vals = collections.defaultdict(list)
    # holds detailed responses for error analysis
    details = collections.defaultdict(list)
    docs = {}
    for task_name, task in task_dict_items:
        versions[task_name] = task.VERSION
        if task.has_test_docs():
            task_doc_func = task.test_docs
        elif task.has_validation_docs():
            task_doc_func = task.validation_docs
        else:
            raise RuntimeError("Task has neither test_docs nor validation_docs")
        task_docs = list(task_doc_func())
        rnd = random.Random()
        rnd.seed(42)

        for doc_id, doc in enumerate(task_docs):
            ctx = task.fewshot_context(
                doc=doc, num_fewshot=num_fewshot, rnd=rnd, description=""
            )
            docs[(task_name, doc_id)] = (doc, ctx)

    for (task_name, doc_id), (doc, ctx) in tqdm(docs.items()):
        task = task_dict[task_name]
        resp = oa_chat_completion(
            engine=engine,
            messages=[{"role": "user", "content": ctx}],
            temperature=0.0,
        )
        # Azure content filter
        if "content" in resp["choices"][0]["message"]:
            resp_txt = resp["choices"][0]["message"]["content"]
        else:
            resp_txt = ""
        choice_found = [
            re.search(req.args[1], resp_txt)
            for req in task.construct_requests(doc, ctx)
        ]
        # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
        result = [
            -1.0 * (m.start() if m is not None else float("inf")) for m in choice_found
        ]
        metrics = task.process_results(doc, result)
        if "details" in metrics:
            details[task_name].append(metrics["details"])
            del metrics["details"]
        for metric, value in metrics.items():
            vals[(task_name, metric)].append(value)

    results: Dict[str, Dict[str, float]] = collections.defaultdict(dict)
    # aggregate results
    for (task_name, metric), items in vals.items():
        task = task_dict[task_name]
        real_metric = metric  # key when looking up the metric with task.aggregation
        results[task_name][metric] = task.aggregation()[real_metric](items)

    final_results = {
        "results": dict(results),
        "versions": dict(versions),
        "config": {
            "model": engine,
            "num_fewshot": num_fewshot,
        },
    }
    dumped = json.dumps(final_results, indent=2, ensure_ascii=False)
    print(dumped)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(dumped)
    print(f"{engine}, " f"num_fewshot: {num_fewshot},")
    print(lm_eval.evaluator.make_table(final_results))


if __name__ == "__main__":
    main()
