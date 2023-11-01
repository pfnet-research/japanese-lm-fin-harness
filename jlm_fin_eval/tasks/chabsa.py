import inspect
import os
from functools import partial
from unittest import result

import numpy as np
from lm_eval.base import MultipleChoiceTask
from lm_eval.base import mean
from lm_eval.base import rf
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import jlm_fin_eval.datasets.chabsa.chabsa


class Chabsa(MultipleChoiceTask):
    VERSION = 1.0
    DATASET_PATH = inspect.getfile(jlm_fin_eval.datasets.chabsa.chabsa)
    DATASET_NAME = "chABSA"
    DESCRIPTION = "以下のセンテンスにおける、ターゲットのセンチメントをpositiveかnegativeで答えてください。\n\n"

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def training_docs(self):
        return None

    def validation_docs(self):
        return None

    def test_docs(self):
        return self.dataset["test"]

    def doc_to_text(self, doc):
        doc_text = f"センテンス: {doc['sentence']}\n"
        doc_text += f"ターゲット: {doc['target']}\n"
        doc_text += "回答: "
        return doc_text

    def doc_to_target(self, doc):
        answer = doc["polarity"]
        return answer

    @staticmethod
    def get_answer(doc):
        return doc["polarity"]

    @staticmethod
    def compute_scores(gold, pred):
        acc = accuracy_score(gold, pred)

        return {"acc": acc}

    def construct_requests(self, doc, ctx):
        lls = [rf.loglikelihood(ctx, choice)[0] for choice in ["positive", "negative"]]

        return lls

    def process_results(self, doc, results):
        gold = doc["polarity"]
        pred = ["positive", "negative"][np.array(results).argmax()]

        out = {
            "acc": (
                pred,
                gold,
            ),
            "f1": (
                pred,
                gold,
            ),
        }
        return out

    def higher_is_better(self):
        return {"acc": True, "f1": True}

    def aggregation(self):
        return {
            "acc": partial(self._chabsa_agg, "acc"),
            "f1": partial(self._chabsa_agg, "f1"),
        }

    def _chabsa_agg(self, key, item):
        predictions, references = zip(*item)
        if key == "acc":
            return (np.asarray(predictions) == np.asarray(references)).mean()
        elif key == "f1":
            return f1_score(references, predictions, average="macro")
        else:
            raise KeyError(key)


class ChabsaWithAnlpPrompt(Chabsa):
    PROMPT_VERSION = 0.1
    DESCRIPTION = "[センテンス]における、[ターゲット]のセンチメントをpositiveかnegativeで選んでください。\n\n"

    def doc_to_text(self, doc):
        doc_text = f"[センテンス]: {doc['sentence']}\n"
        doc_text += f"[ターゲット]: {doc['target']}\n"
        doc_text += "[答え]:"
        return doc_text


class ChabsaWithFintanPrompt(Chabsa):
    PROMPT_VERSION = 0.2
    DESCRIPTION = (
        "センテンスとターゲットを入力として受け取り、ターゲットに関するセンチメントをpositiveかnegativeから選択してください。\n\n"
    )

    def doc_to_text(self, doc):
        doc_text = f"センテンス:{doc['sentence']}\n"
        doc_text += f"ターゲット:{doc['target']}\n"
        doc_text += "回答:"
        return doc_text


class ChabsaWithAlpacaPrompt(Chabsa):
    PROMPT_VERSION = 0.3
    DESCRIPTION = """以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

### 指示:
以下のセンテンスにおける、ターゲットのセンチメントをpositiveかnegativeで答えてください。

"""

    def doc_to_text(self, doc):
        doc_text = f"""### 入力:
センテンス:{doc['sentence']}
ターゲット:{doc['target']}

### 応答:
"""
        return doc_text


class ChabsaWithRinnaInstructionSFT(Chabsa):
    PROMPT_VERSION = 0.4
    DESCRIPTION = (
        f"ユーザー: センテンスにおける、ターゲットのセンチメントをpositiveかnegativeで答えてください。<NL>"
        f"システム: 分かりました。<NL>"
    )
    SEP = "<NL>"
    FEWSHOT_SEP = "<NL>"

    def doc_to_text(self, doc):
        doc_text = (
            f"センテンス: {doc['sentence']}{self.SEP}ターゲット: {doc['target']}{self.SEP}システム: "
        )
        return doc_text


class ChabsaWithRinnaBilingualInstructionSFT(ChabsaWithRinnaInstructionSFT):
    PROMPT_VERSION = 0.5
    DESCRIPTION = "ユーザー: 与えられた文脈から、質問に対する答えを抜き出してください。\nシステム: 分かりました。\n"
    SEP = "\n"
    FEWSHOT_SEP = "\n"


class ChabsaWithLlama2(Chabsa):
    PROMPT_VERSION = 0.6
    DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""
    SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT)
    DESCRIPTION = f"<s>[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n\n"
    INSTRUCTION = "与えられたセンテンスにおける、ターゲットのセンチメントをpositiveかnegativeで答えてください。"
    FEWSHOT_SEP = " </s><s>[INST] "

    def doc_to_text(self, doc):
        input_text = f"センテンス: {doc['sentence'].split('[SEP]')[-1].strip()}\nターゲット: {doc['target']}"
        return f"{self.INSTRUCTION}\n\n{input_text} [/INST] "


VERSIONS = [
    ChabsaWithAnlpPrompt,
    ChabsaWithFintanPrompt,
    ChabsaWithAlpacaPrompt,
    ChabsaWithRinnaInstructionSFT,
    ChabsaWithRinnaBilingualInstructionSFT,
    ChabsaWithLlama2,
]


def construct_tasks():
    tasks = {}
    for version_class in VERSIONS:
        tasks[
            f"chabsa-{version_class.VERSION}-{version_class.PROMPT_VERSION}"
        ] = version_class
    tasks["chabsa"] = Chabsa
    return tasks
