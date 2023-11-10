import collections
import itertools
import random
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from typing import cast

import lm_eval.base
import lm_eval.metrics
import lm_eval.models
import numpy as np
from lm_eval.base import LM
from lm_eval.base import CachingLM
from lm_eval.base import Task
from lm_eval.utils import positional_deprecated
from lm_eval.utils import run_task_tests

import jlm_fin_eval.tasks


@positional_deprecated
def simple_evaluate(
    model: Union[str, LM],
    model_args: Optional[str] = None,
    tasks: List[Union[str, Task]] = [],
    num_fewshot: Union[List[int], int] = 0,
    batch_size: Optional[int] = None,
    device: Optional[str] = None,
    no_cache: bool = False,
    limit: Union[int, List[int | None], None] = None,
    bootstrap_iters: int = 100000,
    description_dict: Optional[Dict[str, str]] = None,
    check_integrity: bool = False,
    decontamination_ngrams_path: Optional[Dict[str, str]] = None,
    verbose: bool = False,
):
    """Instantiate and evaluate a model on a list of tasks.

    :param model: Union[str, LM]
        Name of model or LM object, see lm_eval.models.get_model
    :param model_args: Optional[str]
        String arguments for each model class, see LM.create_from_arg_string.
        Ignored if `model` argument is a LM object.
    :param tasks: list[Union[str, Task]]
        List of task names or Task objects. Task objects will be taken to have name task.EVAL_HARNESS_NAME if defined and type(task).__name__ otherwise.
    :param num_fewshot: int or list of int
        Number of examples in few-shot context
    :param batch_size: int, optional
        Batch size for model
    :param device: str, optional
        PyTorch device (e.g. "cpu" or "cuda:0") for running models
    :param no_cache: bool
        Whether or not to cache
    :param limit: int or list of int, optional
        Limit the number of examples per task (only use this for testing)
    :param bootstrap_iters:
        Number of iterations for bootstrap statistics
    :param description_dict: dict[str, str]
        Dictionary of custom task descriptions of the form: `task_name: description`
    :param check_integrity: bool
        Whether to run the relevant part of the test suite for the tasks
    :return
        Dictionary of results
    """
    random.seed(1234)
    np.random.seed(1234)

    assert tasks != [], "No tasks specified"

    if isinstance(model, str):
        if model_args is None:
            model_args = ""
        lm = lm_eval.models.get_model(model).create_from_arg_string(
            model_args, {"batch_size": batch_size, "device": device}
        )
    else:
        assert isinstance(model, lm_eval.base.LM)
        lm = model

    if not no_cache:
        if model_args is None:
            model_args = ""
        lm = lm_eval.base.CachingLM(
            lm,
            "lm_cache/"
            + str(model)
            + "_"
            + model_args.replace("=", "-").replace(",", "_").replace("/", "-")
            + ".db",
        )

    task_dict = jlm_fin_eval.tasks.get_task_dict(tasks)

    if check_integrity:
        run_task_tests(task_list=[str(task) for task in tasks])

    results: Dict[str, Any] = evaluate(
        lm=lm,
        task_dict=task_dict,
        num_fewshot=num_fewshot,
        limit=limit,
        bootstrap_iters=bootstrap_iters,
        description_dict=description_dict,
        decontamination_ngrams_path=decontamination_ngrams_path,
        verbose=verbose,
    )

    # add info about the model and few shot config
    results["config"] = {
        "model": model,
        "model_args": model_args,
        "num_fewshot": num_fewshot,
        "batch_size": batch_size,
        "device": device,
        "no_cache": no_cache,
        "limit": limit,
        "bootstrap_iters": bootstrap_iters,
        "description_dict": description_dict,
    }

    return results


decontaminate_suffix = "_decontaminate"


@positional_deprecated
def evaluate(
    lm: Union[LM, CachingLM],
    task_dict: Dict[str, Task],
    provide_description: Optional[bool] = None,
    num_fewshot: Union[List[int], int] = 0,
    limit: Union[int, List[int | None], None] = None,
    bootstrap_iters: int = 100000,
    description_dict: Optional[Dict[str, str]] = None,
    decontamination_ngrams_path: Optional[Dict[str, str]] = None,
    verbose: bool = False,
):
    """Instantiate and evaluate a model on a list of tasks.

    :param lm: obj
        Language Model
    :param task_dict: dict[str, Task]
        Dictionary of tasks. Tasks will be taken to have name task.EVAL_HARNESS_NAME if defined and type(task).__name__ otherwise.
    :param provide_description: bool
        Not implemented, and this option is deprecated and will be removed in a future version in favor of a different description providing method
    :param num_fewshot: int or list of int
        Number of examples in few-shot context
    :param limit: int or list of int, optional
        Limit the number of examples per task (only use this for testing)
    :param bootstrap_iters:
        Number of iterations for bootstrap statistics
    :param description_dict: dict[str, str]
        Dictionary of custom task descriptions of the form: `task_name: description`
    :return
        Dictionary of results
    """
    # TODO: completely refactor this entire function to not be a huge mess, ideally breaking it down into smaller pieces

    # TODO: todo: implement proper description-providing system
    assert not provide_description  # not implemented.
    if provide_description is not None:
        # nudge people to not specify it at all
        print(
            "WARNING: provide_description is deprecated and will be removed in a future version in favor of description_dict"
        )
    if isinstance(num_fewshot, list):
        assert len(task_dict) == len(
            num_fewshot
        ), f"The number of tasks ({len(task_dict)}) must be same as the number of elements in `num_fewshot` ({len(num_fewshot)})"
    else:
        # num_fewshot is int
        num_fewshot = [num_fewshot] * len(task_dict)
    if isinstance(limit, list):
        assert len(task_dict) == len(
            limit
        ), f"The number of tasks ({len(task_dict)}) must be same as the number of elements in `num_fewshot` ({len(limit)})"
    else:
        # limit is int or None
        limit = [limit] * len(task_dict)

    decontaminate = decontamination_ngrams_path is not None

    task_dict_items = [
        (name, task)
        for name, task in task_dict.items()
        if (task.has_validation_docs() or task.has_test_docs())
    ]

    results = collections.defaultdict(dict)
    versions = collections.defaultdict(dict)

    requests = collections.defaultdict(list)
    requests_origin = collections.defaultdict(list)

    overlaps = collections.defaultdict(list)  # {task_name: contaminated_docs}

    # If we ever run into issues where the eval tasks don't fit in memory and we can't afford a machine with bigger
    # memory, we can always modify this plumbing to support that, but I didn't want to include it just yet because
    # over-engineering is bad (or we could make it write the requests to disk and then read them back out again
    #  - probably using an sqlite db because of all the moving parts we have

    # TODO: we need unit tests & sanity checks or something to ensure that the return of `validation_docs` is stable
    docs = {}

    docs_for_decontamination = collections.defaultdict(list)

    # get lists of each type of request
    for idx, (task_name, task) in enumerate(task_dict_items):
        versions[task_name] = task.VERSION  # type: ignore
        # default to test doc, fall back to val doc if validation unavailable
        # TODO: the test-fallback-to-val system isn't final, we should revisit it at some point
        if task.has_test_docs():
            task_doc_func = task.test_docs
            task_set = "test"  # Required for caching in the decontamination
        elif task.has_validation_docs():
            task_set = "val"  # Required for caching in the decontamination
            task_doc_func = task.validation_docs
        else:
            raise RuntimeError("Task has neither test_docs nor validation_docs")

        # deterministically shuffle docs and chop off the first `limit` because sometimes docs are in some kind of order
        task_docs = list(task_doc_func())
        rnd = random.Random()
        rnd.seed(42)
        rnd.shuffle(task_docs)

        description = (
            description_dict[task_name]
            if description_dict and task_name in description_dict
            else ""
        )
        # set tokenizer inside task
        if task.LOAD_TOKENIZER:
            if isinstance(lm, lm_eval.base.CachingLM):
                task.set_tokenizer(lm.lm.tokenizer)
            else:
                task.set_tokenizer(lm.tokenizer)  # type: ignore
        # set max_length to task object
        task.max_length = (  # type: ignore
            lm.lm.max_length
            if isinstance(lm, lm_eval.base.CachingLM)
            else lm.max_length  # type: ignore
        )
        task.max_gen_toks = (  # type: ignore
            lm.lm.max_gen_toks
            if isinstance(lm, lm_eval.base.CachingLM)
            else lm.max_gen_toks  # type: ignore
        )

        limit_local = limit[idx]
        if isinstance(limit_local, float):
            limit_local = int(limit_local * len(task_docs))
            print(
                f"Use {limit_local}/{len(task_docs)} samples corresponding to the ratio of {limit[idx]}"
            )
        for doc_id, doc in enumerate(itertools.islice(task_docs, 0, limit_local)):
            if decontaminate and task.should_decontaminate():
                docs_for_decontamination[(task_name, task_set)].append(
                    task.doc_to_decontamination_query(doc)
                )

            docs[(task_name, doc_id)] = doc
            ctx = task.fewshot_context(
                doc=doc, num_fewshot=num_fewshot[idx], rnd=rnd, description=description
            )
            reqs = task.construct_requests(doc, ctx)
            if not isinstance(reqs, (list, tuple)):
                reqs = [reqs]
            for i, req in enumerate(reqs):
                requests[req.request_type].append(req)  # type: ignore
                # i: index in requests for a single task instance
                # doc_id: unique id that we can get back to a doc using `docs`
                requests_origin[req.request_type].append((i, task_name, doc, doc_id))  # type: ignore

    # Compare all tasks/sets at once to ensure a single training set scan
    if decontaminate:
        from lm_eval.decontamination.decontaminate import get_train_overlap

        print("Finding train/test overlap, please wait...")
        overlaps = get_train_overlap(
            docs_for_decontamination, decontamination_ngrams_path, limit
        )

    # all responses for each (task, doc)
    process_res_queue = collections.defaultdict(list)

    # execute each type of request
    for reqtype, reqs in requests.items():
        # TODO: right now, this code runs multiple separate LM requests for multiple Requests differing
        #       only in index. We could implement some kind of caching, but that would be more of a band-aid
        #       solution. we could also implement some kind of auto-grouping here;
        #       they should end up next to each other.

        print("Running", reqtype, "requests")
        resps = getattr(lm, reqtype)([req.args for req in reqs])
        resps = [
            x if req.index is None else x[req.index] for x, req in zip(resps, reqs)
        ]

        for resp, (i, task_name, doc, doc_id) in zip(resps, requests_origin[reqtype]):
            process_res_queue[(task_name, doc_id)].append((i, resp))

    vals = collections.defaultdict(list)
    # holds detailed responses for error analysis
    details = collections.defaultdict(list)

    # unpack results and sort back in order and return control to Task
    for (task_name, doc_id), requests in process_res_queue.items():
        requests.sort(key=lambda x: x[0])
        requests = [x[1] for x in requests]

        task = task_dict[task_name]
        doc = docs[(task_name, doc_id)]

        metrics: Dict[str, Any] = cast(
            Dict[str, Any], task.process_results(doc, requests)
        )
        if "details" in metrics:
            details[task_name].append(metrics["details"])
            del metrics["details"]
        for metric, value in metrics.items():
            vals[(task_name, metric)].append(value)

            # Re-use the evaluation for the decontaminated set by just ignoring the overlaps
            if decontaminate and task_name in overlaps:
                if doc_id not in overlaps[task_name]:
                    vals[(task_name, metric + decontaminate_suffix)].append(value)

    # aggregate results
    for (task_name, metric), items in vals.items():
        task: Task = task_dict[task_name]
        real_metric = metric  # key when looking up the metric with task.aggregation
        if metric.endswith(decontaminate_suffix):
            real_metric = metric.replace(
                decontaminate_suffix, ""
            )  # decontaminated still uses the same metric
        results[task_name][metric] = cast(Dict, task.aggregation())[real_metric](items)

        # hotfix: bleu, chrf, ter seem to be really expensive to bootstrap
        # so we run them less iterations. still looking for a cleaner way to do this

        stderr = lm_eval.metrics.stderr_for_metric(
            metric=cast(Dict, task.aggregation())[real_metric],
            bootstrap_iters=min(bootstrap_iters, 1000)
            if metric in ["bleu", "chrf", "ter"]
            else bootstrap_iters,
        )

        if stderr is not None:
            results[task_name][metric + "_stderr"] = stderr(items)

        if verbose and task_name in details:
            results[task_name]["details"] = details[task_name]

    return {"results": dict(results), "versions": dict(versions)}


def make_table(result_dict):
    """Generate table of results."""
    from pytablewriter import LatexTableWriter
    from pytablewriter import MarkdownTableWriter

    md_writer = MarkdownTableWriter()
    latex_writer = LatexTableWriter()
    md_writer.headers = ["Task", "Version", "Metric", "Value", "", "Stderr"]
    latex_writer.headers = ["Task", "Version", "Metric", "Value", "", "Stderr"]

    values = []

    for k, dic in result_dict["results"].items():
        version = result_dict["versions"][k]
        for m, v in dic.items():
            if m == "details":
                continue

            if m.endswith("_stderr"):
                continue

            if m + "_stderr" in dic:
                se = dic[m + "_stderr"]
                values.append([k, version, m, "%.4f" % v, "±", "%.4f" % se])
            else:
                values.append([k, version, m, "%.4f" % v, "", ""])
            k = ""
            version = ""
    md_writer.value_matrix = values
    latex_writer.value_matrix = values

    # todo: make latex table look good
    # print(latex_writer.dumps())

    return md_writer.dumps()
