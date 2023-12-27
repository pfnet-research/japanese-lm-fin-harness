import argparse
import fnmatch
import json
import os
from typing import Iterator
from typing import List

import openai
from lm_eval import utils
from lm_eval.models.gpt3 import GPT3LM
from lm_eval.models.gpt3 import get_result
from lm_eval.models.gpt3 import oa_completion
from tqdm import tqdm
from transformers.models.auto.tokenization_auto import AutoTokenizer

from jlm_fin_eval import evaluator
from jlm_fin_eval import tasks

openai.api_type = os.environ.get("OPENAI_API_TYPE", "open_ai")
openai.api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
openai.api_version = os.environ.get("OPENAI_API_VERSION")
openai.api_key = os.environ.get("OPENAI_API_SECRET_KEY")


def from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs):
    return AutoTokenizer._from_pretrained(
        pretrained_model_name_or_path, *inputs, trust_remote_code=True, **kwargs
    )


class MultiChoice:
    def __init__(self, choices: List[str]) -> None:
        self.choices = choices

    # Simple wildcard support (linux filename patterns)
    def __contains__(self, values: str) -> bool:
        for value in values.split(","):
            if len(fnmatch.filter(self.choices, value)) == 0:
                return False

        return True

    def __iter__(self) -> Iterator[str]:
        for choice in self.choices:
            yield choice


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--model_args", default="")
    parser.add_argument("--tasks", default=None, choices=MultiChoice(tasks.ALL_TASKS))
    parser.add_argument("--provide_description", action="store_true")
    parser.add_argument("--num_fewshot", type=str, default="0")
    parser.add_argument("--batch_size", type=int, default=None)
    parser.add_argument("--device", type=str, default=None)
    parser.add_argument("--output_path", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--no_cache", action="store_true")
    parser.add_argument("--decontamination_ngrams_path", default=None)
    parser.add_argument("--description_dict_path", default=None)
    parser.add_argument("--check_integrity", action="store_true")

    return parser.parse_args()


# Returns a list containing all values of the source_list that
# match at least one of the patterns
def pattern_match(patterns: List[str], source_list: List[str]) -> List[str]:
    task_names = set()
    for pattern in patterns:
        for matching in fnmatch.filter(source_list, pattern):
            task_names.add(matching)
    return sorted(list(task_names))


def _loglikelihood_tokens(self, requests, disable_tqdm=False):
    res = []

    def _collate(x):
        # this doesn't efficiently handle last-token differences yet, but those are kinda annoying because
        # it's not guaranteed that the 100 or so logprobs we get to see actually contain all the continuations
        # we care about and so we need some kind of backup for when it isn't
        toks = x[1] + x[2]
        return -len(toks), tuple(toks)

    re_ord = utils.Reorderer(requests, _collate)

    for chunk in tqdm(
        list(utils.chunks(re_ord.get_reordered(), self.REQ_CHUNK_SIZE)),
        disable=disable_tqdm,
    ):
        inps = []
        ctxlens = []
        for cache_key, context_enc, continuation_enc in chunk:
            # max_length+1 because the API takes up to 2049 tokens, including the first context token
            inp = (context_enc + continuation_enc)[-(self.max_length + 1) :]
            # TODO: the logic is much simpler if we just look at the length of continuation tokens
            ctxlen = len(context_enc) - max(
                0, len(context_enc) + len(continuation_enc) - (self.max_length + 1)
            )

            inps.append(inp)
            ctxlens.append(ctxlen)

        response = oa_completion(
            engine=self.engine,
            prompt=[self.tok_decode(inp) for inp in inps],
            echo=True,
            max_tokens=0,
            temperature=0.0,
            logprobs=10,
        )

        for resp, ctxlen, (cache_key, context_enc, continuation_enc) in zip(
            response.choices, ctxlens, chunk
        ):
            answer = get_result(resp, ctxlen)

            res.append(answer)

            # partial caching
            if cache_key is not None:
                self.cache_hook.add_partial("loglikelihood", cache_key, answer)

    return re_ord.get_original(res)


GPT3LM._loglikelihood_tokens = _loglikelihood_tokens


def main() -> None:
    args = parse_args()

    assert not args.provide_description  # not implemented

    if "trust_remote_code=True" in args.model_args:
        AutoTokenizer._from_pretrained = AutoTokenizer.from_pretrained
        AutoTokenizer.from_pretrained = from_pretrained

    if args.limit:
        print(
            "WARNING: --limit SHOULD ONLY BE USED FOR TESTING. REAL METRICS SHOULD NOT BE COMPUTED USING LIMIT."
        )

    if args.tasks is None:
        task_names = tasks.ALL_TASKS
    else:
        task_names = pattern_match(args.tasks.split(","), tasks.ALL_TASKS)

    print(f"Selected Tasks: {task_names}")

    if args.num_fewshot is not None:
        num_fewshot = [int(n) for n in args.num_fewshot.split(",")]
        if len(args.num_fewshot) == 1:
            num_fewshot = [num_fewshot[0] for _ in task_names]
    else:
        num_fewshot = [0 for _ in task_names]

    description_dict = {}
    if args.description_dict_path:
        with open(args.description_dict_path, "r") as f:
            description_dict = json.load(f)

    results = evaluator.simple_evaluate(
        model=args.model,
        model_args=args.model_args,
        tasks=task_names,
        num_fewshot=num_fewshot,
        batch_size=args.batch_size,
        device=args.device,
        no_cache=args.no_cache,
        limit=args.limit,
        description_dict=description_dict,
        decontamination_ngrams_path=args.decontamination_ngrams_path,
        check_integrity=args.check_integrity,
    )

    dumped = json.dumps(results, indent=2)
    print(dumped)

    if args.output_path:
        with open(args.output_path, "w") as f:
            f.write(dumped)

    print(
        f"{args.model} ({args.model_args}), limit: {args.limit}, provide_description: {args.provide_description}, "
        f"num_fewshot: {args.num_fewshot}, batch_size: {args.batch_size}"
    )
    print(evaluator.make_table(results))


if __name__ == "__main__":
    main()
