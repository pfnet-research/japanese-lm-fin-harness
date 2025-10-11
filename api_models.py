import os
import re
import time
import unicodedata
from collections import defaultdict
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Tuple

import anthropic
import lm_eval.evaluator
import openai
import vertexai
import vertexai.preview.generative_models
from lm_eval.__main__ import parse_eval_args
from lm_eval.__main__ import setup_parser
from lm_eval.models.anthropic_llms import AnthropicLM
from lm_eval.models.openai_completions import LocalCompletionsAPI
from ray import client
from tqdm import tqdm

from main import cli_evaluate

base_url = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
openai.api_type = os.environ.get("OPENAI_API_TYPE", "openai")
openai.api_version = os.environ.get("OPENAI_API_VERSION")
openai.api_key = os.environ.get("OPENAI_API_KEY")

GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
GCP_REGION = os.environ.get("GCP_REGION")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def oa_chat_completion(
    client: openai.Client, chat: bool = False, **kwargs: Any
) -> Optional[Dict]:
    """Query OpenAI API for completion.

    Retry with back-off until they respond
    """
    backoff_time = 3.0
    while True:
        try:
            if chat:
                return client.chat.completions.create(**kwargs)
            else:
                return client.completions.create(**kwargs)
        except openai.OpenAIError as e:
            if e.code == "content_filter":
                return None
            import traceback

            traceback.print_exc()
            time.sleep(backoff_time)
            backoff_time *= 1.5


def vertexai_chat_completion(
    client: vertexai.generative_models.GenerativeModel, **kwargs: Any
) -> Optional[Dict]:
    backoff_time = 3.0
    while True:
        try:
            return client.generate_content(**kwargs)
        except:
            import traceback

            traceback.print_exc()
            time.sleep(backoff_time)
            backoff_time *= 1.5


def anthropic_completion(client: anthropic.Anthropic, **kwargs: Any) -> Optional[Dict]:
    backoff_time = 3.0
    while True:
        try:
            return client.messages.create(**kwargs)
        except:
            import traceback

            traceback.print_exc()
            time.sleep(backoff_time)
            backoff_time *= 1.5


class AzureOpenaiCompletionsLM(LocalCompletionsAPI):
    MULTIMODAL = False

    def __init__(
        self,
        model: str,
        base_url: str,
        tokenizer: Optional[str] = None,
        tokenizer_backend: Literal["tiktoken", "huggingface"] = "tiktoken",
        truncate: bool = False,
        max_gen_toks: int = 256,
        batch_size: int = 1,
        seed: int = 1234,
        max_length: Optional[int] = 2048,
    ) -> None:
        super().__init__(
            model=model,
            base_url=base_url,
            tokenizer=tokenizer,
            tokenizer_backend=tokenizer_backend,
            truncate=truncate,
            max_gen_toks=max_gen_toks,
            batch_size=batch_size,
            seed=seed,
            max_length=max_length,
        )
        self.client = openai.AzureOpenAI(
            azure_endpoint=self.base_url,
            api_key=os.environ.get("OPENAI_API_KEY"),
            api_version=os.environ.get("OPENAI_API_VERSION"),
        )

    def _loglikelihood_tokens(
        self,
        requests: List[Tuple[Tuple[str, str], List[int], List[int]]],
        disable_tqdm: bool = False,
        override_bs: int = None,
    ) -> List[Tuple[float, bool]]:
        res = defaultdict(list)

        grouper = lm_eval.models.utils.Grouper(requests, lambda x: str(x[0][0]))

        pbar = tqdm(total=len(requests), disable=(disable_tqdm or (self.rank != 0)))
        for key, re_ord in grouper.get_grouped().items():
            inps = [{"role": "user", "content": key}]

            response = oa_chat_completion(
                client=self.client,
                chat=True,
                messages=inps,
                model=self.model,
                temperature=0.0,
                max_tokens=self.max_gen_toks,
            )

            # Azure content filter
            if response is not None and response.choices[0].message.content:
                resp_txt = response.choices[0].message.content
            else:
                resp_txt = ""
            choices = list(
                map(
                    lambda x: x[1:] if x[0] == " " else x,
                    map(lambda x: x[0][1], re_ord),
                )
            )
            choice_found = [re.search(choice, resp_txt) for choice in choices]
            # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
            result = [
                -1.0 * (m.start() if m is not None else float("inf"))
                for m in choice_found
            ]

            for ll, ord in zip(result, re_ord):
                answer = (ll, ll == max(result))
                res[key].append(answer)
                self.cache_hook.add_partial("loglikelihood", ord[0], answer)
                pbar.update(1)

        pbar.close()

        return grouper.get_original(res)


class GcpVertexAiCompletionsLM(LocalCompletionsAPI):
    """GCP VertexAI completions model.

    ```
    gcloud auth application-default login
    ```
    is necessary to authenticate the GCP account.
    """

    MULTIMODAL = False

    def __init__(
        self,
        model: str,
        base_url: str = None,
        tokenizer: Optional[str] = None,
        tokenizer_backend: Literal["tiktoken", "huggingface"] = "tiktoken",
        truncate: bool = False,
        max_gen_toks: int = 256,
        batch_size: int = 1,
        seed: int = 1234,
        max_length: Optional[int] = 2048,
    ) -> None:
        os.environ["OPENAI_API_KEY"] = "DUMMY_KEY"
        super().__init__(
            model="gpt-35-turbo",
            base_url=base_url,
            tokenizer=tokenizer,
            tokenizer_backend=tokenizer_backend,
            truncate=truncate,
            max_gen_toks=max_gen_toks,
            batch_size=batch_size,
            seed=seed,
            max_length=max_length,
        )
        self.model = model
        vertexai.init(project=GCP_PROJECT_ID, location=GCP_REGION)
        self.client = vertexai.preview.generative_models.GenerativeModel(
            model_name=self.model,
            generation_config=vertexai.preview.generative_models.GenerationConfig(
                temperature=0.0, max_output_tokens=self.max_gen_toks
            ),
            safety_settings={
                vertexai.preview.generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: vertexai.preview.generative_models.HarmBlockThreshold.BLOCK_NONE,
                vertexai.preview.generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: vertexai.preview.generative_models.HarmBlockThreshold.BLOCK_NONE,
                vertexai.preview.generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: vertexai.preview.generative_models.HarmBlockThreshold.BLOCK_NONE,
                vertexai.preview.generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: vertexai.preview.generative_models.HarmBlockThreshold.BLOCK_NONE,
                vertexai.preview.generative_models.HarmCategory.HARM_CATEGORY_UNSPECIFIED: vertexai.preview.generative_models.HarmBlockThreshold.BLOCK_NONE,
            },
        )

    def _loglikelihood_tokens(
        self,
        requests: List[Tuple[Tuple[str, str], List[int], List[int]]],
        disable_tqdm: bool = False,
        override_bs: int = None,
    ) -> List[Tuple[float, bool]]:
        res = defaultdict(list)

        grouper = lm_eval.models.utils.Grouper(requests, lambda x: str(x[0][0]))

        pbar = tqdm(total=len(requests), disable=(disable_tqdm or (self.rank != 0)))
        for key, re_ord in grouper.get_grouped().items():
            response = vertexai_chat_completion(
                client=self.client,
                contents=vertexai.preview.generative_models.Part.from_text(key),
            )

            if response is not None and response.candidates[0].content.parts[0].text:
                resp_txt = response.candidates[0].content.parts[0].text
            else:
                resp_txt = ""
            choices = list(
                map(
                    lambda x: x[1:] if x[0] == " " else x,
                    map(lambda x: x[0][1], re_ord),
                )
            )
            choice_found = [re.search(choice, resp_txt) for choice in choices]
            # workaround for gemini
            choice_found2 = [
                re.search(unicodedata.normalize("NFKC", choice), resp_txt)
                for choice in choices
            ]
            # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
            result = [
                max(
                    -1.0 * (m.start() if m is not None else float("inf")),
                    -1.0 * (m2.start() if m2 is not None else float("inf")),
                )
                for m, m2 in zip(choice_found, choice_found2)
            ]

            for ll, ord in zip(result, re_ord):
                answer = (ll, ll == max(result))
                res[key].append(answer)
                self.cache_hook.add_partial("loglikelihood", ord[0], answer)
                pbar.update(1)

        pbar.close()

        return grouper.get_original(res)


class CustomizedAnthropicLM(AnthropicLM):
    MULTIMODAL = False

    def loglikelihood(self, requests: List) -> List[Tuple[float, bool]]:
        res = defaultdict(list)

        grouper = lm_eval.models.utils.Grouper(requests, lambda x: str(x.args[0]))

        pbar = tqdm(total=len(requests))
        for key, re_ord in grouper.get_grouped().items():
            inps = [{"role": "user", "content": key}]

            response = anthropic_completion(
                client=self.client,
                model=self.model,
                messages=inps,
                temperature=0.0,
                max_tokens=self.max_gen_toks,
            )

            if response is not None and response.content[0].text:
                resp_txt = response.content[0].text
            else:
                resp_txt = ""
            choices = list(
                map(
                    lambda x: x[1:] if x[0] == " " else x,
                    map(lambda x: x.args[1], re_ord),
                )
            )
            choice_found = [re.search(choice, resp_txt) for choice in choices]
            # workaround for gemini
            choice_found2 = [
                re.search(unicodedata.normalize("NFKC", choice), resp_txt)
                for choice in choices
            ]
            # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
            result = [
                max(
                    -1.0 * (m.start() if m is not None else float("inf")),
                    -1.0 * (m2.start() if m2 is not None else float("inf")),
                )
                for m, m2 in zip(choice_found, choice_found2)
            ]

            for ll, ord in zip(result, re_ord):
                answer = (ll, ll == max(result))
                res[key].append(answer)
                self.cache_hook.add_partial("loglikelihood", ord.args, answer)
                pbar.update(1)

        pbar.close()

        return grouper.get_original(res)


class SelfHostedCompletionsLM1(LocalCompletionsAPI):
    MULTIMODAL = False

    def __init__(
        self,
        model: str,
        base_url: str,
        tokenizer: Optional[str] = None,
        tokenizer_backend: Literal["tiktoken", "huggingface"] = "tiktoken",
        truncate: bool = False,
        max_gen_toks: int = 256,
        batch_size: int = 1,
        seed: int = 1234,
        max_length: Optional[int] = 2048,
    ) -> None:
        super().__init__(
            model="gpt-35-turbo",
            base_url=base_url,
            tokenizer=tokenizer,
            tokenizer_backend=tokenizer_backend,
            truncate=truncate,
            max_gen_toks=max_gen_toks,
            batch_size=batch_size,
            seed=seed,
            max_length=max_length,
        )
        self.model = model
        self.client = openai.OpenAI(
            base_url=self.base_url,
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def _loglikelihood_tokens(
        self,
        requests: List[Tuple[Tuple[str, str], List[int], List[int]]],
        disable_tqdm: bool = False,
        override_bs: int = None,
    ) -> List[Tuple[float, bool]]:
        res = defaultdict(list)

        grouper = lm_eval.models.utils.Grouper(requests, lambda x: str(x[0][0]))

        pbar = tqdm(total=len(requests), disable=(disable_tqdm or (self.rank != 0)))
        for key, re_ord in grouper.get_grouped().items():
            response = oa_chat_completion(
                client=self.client,
                chat=False,
                prompt=key,
                model=self.model,
                temperature=0.0,
                max_tokens=self.max_gen_toks,
            )

            # Azure content filter
            if response is not None and response.choices[0].text:
                resp_txt = response.choices[0].text
            else:
                resp_txt = ""
            choices = list(
                map(
                    lambda x: x[1:] if x[0] == " " else x,
                    map(lambda x: x[0][1], re_ord),
                )
            )
            choice_found = [re.search(choice, resp_txt) for choice in choices]
            # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
            result = [
                -1.0 * (m.start() if m is not None else float("inf"))
                for m in choice_found
            ]

            for ll, ord in zip(result, re_ord):
                answer = (ll, ll == max(result))
                res[key].append(answer)
                self.cache_hook.add_partial("loglikelihood", ord[0], answer)
                pbar.update(1)

        pbar.close()

        return grouper.get_original(res)


class SelfHostedChatCompletionsLM1(LocalCompletionsAPI):
    MULTIMODAL = False

    def __init__(
        self,
        model: str,
        base_url: str,
        tokenizer: Optional[str] = None,
        tokenizer_backend: Literal["tiktoken", "huggingface"] = "tiktoken",
        truncate: bool = False,
        max_gen_toks: int = 256,
        batch_size: int = 1,
        seed: int = 1234,
        max_length: Optional[int] = 2048,
    ) -> None:
        super().__init__(
            model="gpt-35-turbo",
            base_url=base_url,
            tokenizer=tokenizer,
            tokenizer_backend=tokenizer_backend,
            truncate=truncate,
            max_gen_toks=max_gen_toks,
            batch_size=batch_size,
            seed=seed,
            max_length=max_length,
        )
        self.model = model
        self.client = openai.OpenAI(
            base_url=self.base_url,
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.temperature = 0.0
        if model == "nvidia/nemotron-4-340b-instruct":
            self.temperature = 0.000001

    def _loglikelihood_tokens(
        self,
        requests: List[Tuple[Tuple[str, str], List[int], List[int]]],
        disable_tqdm: bool = False,
        override_bs: int = None,
    ) -> List[Tuple[float, bool]]:
        res = defaultdict(list)

        grouper = lm_eval.models.utils.Grouper(requests, lambda x: str(x[0][0]))

        pbar = tqdm(total=len(requests), disable=(disable_tqdm or (self.rank != 0)))
        for key, re_ord in grouper.get_grouped().items():
            inps = [{"role": "user", "content": key}]

            response = oa_chat_completion(
                client=self.client,
                chat=True,
                messages=inps,
                model=self.model,
                temperature=0.0,
                max_tokens=self._max_gen_toks,
            )

            # Azure content filter
            if response is not None and response.choices[0].message.content:
                resp_txt = response.choices[0].message.content
            else:
                resp_txt = ""
            choices = list(
                map(
                    lambda x: x[1:] if x[0] == " " else x,
                    map(lambda x: x[0][1], re_ord),
                )
            )
            choice_found = [re.search(choice, resp_txt) for choice in choices]
            # Note: if the task employs likelihood, -1.0 is multiplied. But, others are dependent on the task.
            result = [
                -1.0 * (m.start() if m is not None else float("inf"))
                for m in choice_found
            ]

            for ll, ord in zip(result, re_ord):
                answer = (ll, ll == max(result))
                res[key].append(answer)
                self.cache_hook.add_partial("loglikelihood", ord[0], answer)
                pbar.update(1)

        pbar.close()

        return grouper.get_original(res)


if __name__ == "__main__":
    parser = setup_parser()
    args = parse_eval_args(parser)
    if args.model is None or args.model == "openai":
        args.model = AzureOpenaiCompletionsLM.create_from_arg_string(
            args.model_args, {"base_url": base_url}
        )
    elif args.model == "vertexai":
        args.model = GcpVertexAiCompletionsLM.create_from_arg_string(args.model_args)
    elif args.model == "anthropic":
        args.model = CustomizedAnthropicLM.create_from_arg_string(args.model_args)
    elif args.model == "self-hosted-1":
        args.model = SelfHostedCompletionsLM1.create_from_arg_string(
            args.model_args, {"base_url": base_url}
        )
    elif args.model == "self-hosted-chat-1":
        args.model = SelfHostedChatCompletionsLM1.create_from_arg_string(
            args.model_args, {"base_url": base_url}
        )
    else:
        raise NotImplementedError("openai, vertexai, and anthropic are supported")
    cli_evaluate(args=args)
