import argparse
import collections
import fnmatch
import itertools
import logging
import random

import jlm_fin_eval.tasks

logging.getLogger("openai").setLevel(logging.WARNING)


class MultiChoice:
    def __init__(self, choices):
        self.choices = choices

    # Simple wildcard support (linux filename patterns)
    def __contains__(self, values):
        for value in values.split(","):
            if len(fnmatch.filter(self.choices, value)) == 0:
                return False

        return True

    def __iter__(self):
        for choice in self.choices:
            yield choice


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tasks", default=None, choices=MultiChoice(jlm_fin_eval.tasks.ALL_TASKS)
    )
    parser.add_argument("--num_fewshot", type=int, default=0)

    return parser.parse_args()


# Returns a list containing all values of the source_list that
# match at least one of the patterns
def pattern_match(patterns, source_list):
    task_names = set()
    for pattern in patterns:
        for matching in fnmatch.filter(source_list, pattern):
            task_names.add(matching)
    return list(task_names)


def main():
    args = parse_args()

    if args.tasks is None:
        task_names = jlm_fin_eval.tasks.ALL_TASKS
    else:
        task_names = pattern_match(args.tasks.split(","), jlm_fin_eval.tasks.ALL_TASKS)

    print(f"Selected Tasks: {task_names}")

    tasks = task_names
    num_fewshot = args.num_fewshot

    task_dict = jlm_fin_eval.tasks.get_task_dict(tasks)

    task_dict_items = [
        (name, task)
        for name, task in task_dict.items()
        if (task.has_validation_docs() or task.has_test_docs())
    ]
    requests = collections.defaultdict(list)
    requests_origin = collections.defaultdict(list)
    docs = {}
    for task_name, task in task_dict_items:
        if task.has_test_docs():
            task_doc_func = task.test_docs
        elif task.has_validation_docs():
            task_doc_func = task.validation_docs
        else:
            raise RuntimeError("Task has neither test_docs nor validation_docs")
        task_docs = list(task_doc_func())
        rnd = random.Random()
        rnd.seed(42)

        for doc_id, doc in enumerate(itertools.islice(task_docs, 0, 1)):
            ctx = task.fewshot_context(
                doc=doc, num_fewshot=num_fewshot, rnd=rnd, description=""
            )
            docs[(task_name, doc_id)] = doc
            reqs = task.construct_requests(doc, ctx)
            if not isinstance(reqs, (list, tuple)):
                reqs = [reqs]
            for i, req in enumerate(reqs):
                requests[req.request_type].append(req)
                # i: index in requests for a single task instance
                # doc_id: unique id that we can get back to a doc using `docs`
                requests_origin[req.request_type].append((i, task_name, doc, doc_id))
            # all responses for each (task, doc)
    process_res_queue = collections.defaultdict(list)

    print_dict = {}
    # execute each type of request
    for reqtype, reqs in requests.items():
        for req, (i, task_name, doc, doc_id) in zip(reqs, requests_origin[reqtype]):
            process_res_queue[(task_name, doc_id)].append((i, req))
            task = task_dict[task_name]
            print_text = "=========================\n"
            print_text += task_name + "\n"
            print_text += "----------input-----------\n"
            print_text += str(req.args[0]) + "{answe will be placed here}" + "\n"
            print_text += "----------answer----------\n"
            print_text += req.args[1] + "\n"
            print_text += "----------metrics---------"
            print_dict[(task_name, doc_id, i)] = print_text

    for (task_name, doc_id), requests in process_res_queue.items():
        requests.sort(key=lambda x: x[0])
        requests = [x[1] for x in requests]

        task = task_dict[task_name]
        doc = docs[(task_name, doc_id)]

        answer = task.doc_to_target(doc)
        results = [0.0 if x.args[1] == answer else -1.0 for x in requests]
        try:
            answer_index = results.index(0.0)
        except Exception as e:
            print(f"error in {task_name}: \n{requests}\n{answer}")
            raise e

        metrics = task.process_results(doc, results)
        print(print_dict[(task_name, doc_id, answer_index)])
        print(metrics)


if __name__ == "__main__":
    main()
