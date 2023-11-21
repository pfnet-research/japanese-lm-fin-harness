import inspect
import os

import numpy as np
from lm_eval.base import MultipleChoiceTask
from lm_eval.base import mean
from lm_eval.base import rf
from sklearn.metrics import accuracy_score

import jlm_fin_eval.datasets.fp2.fp2


class FP2(MultipleChoiceTask):
    VERSION = 1.0
    DATASET_PATH = inspect.getfile(jlm_fin_eval.datasets.fp2.fp2)
    DATASET_NAME = "fp2"
    DESCRIPTION = "以下の問題の適切な答えを選択肢から選んで１～４の数字で答えなさい。\n\n"

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
        doc_text = "【問題】\n" + doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            doc_text += doc["context"] + "\n"
        doc_text += "\n【答え】\n"
        # doc_text += chr(int(doc["answer"]) + 65)
        return doc_text

    def doc_to_target(self, doc):
        answer = doc["choices"]["text"][doc["choices"]["id"].index(doc["answer"])]
        return answer

    @staticmethod
    def compute_scores(gold, pred):
        acc = accuracy_score(gold, pred)

        return {"acc": acc}

    def construct_requests(self, doc, ctx):
        lls = [rf.loglikelihood(ctx, choice)[0] for choice in doc["choices"]["text"]]

        return lls

    def process_results(self, doc, results):
        gold = doc["answer"]

        acc = 1.0 if doc["choices"]["id"][np.argmax(results)] == gold else 0.0
        ranking = [doc["choices"]["id"][i] for i in np.argsort(results)[::-1]]
        correct_answer_ranking = ranking.index(gold) + 1
        map_score = 1.0 / correct_answer_ranking
        map_2 = 0.0 if correct_answer_ranking > 2 else map_score
        map_3 = 0.0 if correct_answer_ranking > 3 else map_score
        map_4 = 0.0 if correct_answer_ranking > 4 else map_score

        return {
            "acc": acc,
            "map": map_score,
            "map_2": map_2,
            "map_3": map_3,
            "map_4": map_4,
        }

    def higher_is_better(self):
        return {"acc": True, "map": True, "map_2": True, "map_3": True, "map_4": True}

    def aggregation(self):
        return {
            "acc": mean,
            "map": mean,
            "map_2": mean,
            "map_3": mean,
            "map_4": mean,
        }


class FP2WithAnlpPrompt(FP2):
    PROMPT_VERSION = 0.1
    DESCRIPTION = "[問題]に対する[答え]を[選択肢]の中から選んでください。\n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        return f"[問題]:{q_doc_text}[選択肢]:[{', '.join(doc['choices']['text'])}]\n[答え]:"

    def doc_to_target(self, doc):
        return [
            choice_text
            for choice_id, choice_text in zip(
                doc["choices"]["id"], doc["choices"]["text"]
            )
            if choice_id == doc["answer"]
        ][0]

    def construct_requests(self, doc, ctx):
        lls = [rf.loglikelihood(ctx, choice)[0] for choice in doc["choices"]["text"]]

        return lls


class FP2WithAnlpPromptAlphabet(FP2):
    PROMPT_VERSION = "0.1.2"
    DESCRIPTION = "[問題]に対する[答え]を[選択肢]の中からアルファベットで選んでください。\n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choice_doc_text = []
        for choice_id, choice_text in zip(doc["choices"]["id"], doc["choices"]["text"]):
            choice_doc_text.append(chr(choice_id + 65) + ":" + choice_text)
        return f"[問題]:{q_doc_text}[選択肢]:[{', '.join(choice_doc_text)}]\n[答え]:"


class FP2WithFintanPrompt(FP2):
    PROMPT_VERSION = 0.2
    DESCRIPTION = "質問と回答の選択肢を入力として受け取り、選択肢から回答を選択してください。なお、回答は選択肢の番号(例:0)でするものとします。\n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choices = ",".join(
            [
                f"{idx}.{choice}"
                for idx, choice in zip(doc["choices"]["id"], doc["choices"]["text"])
            ]
        )
        return f"質問:{q_doc_text}" f"選択肢:{choices}\n" "回答:"

    def doc_to_target(self, doc):
        return [
            str(choice_id)
            for choice_id in doc["choices"]["id"]
            if choice_id == doc["answer"]
        ][0]

    def construct_requests(self, doc, ctx):
        lls = [rf.loglikelihood(ctx, str(choice))[0] for choice in doc["choices"]["id"]]

        return lls


class FP2WithFintanPromptV1(FP2WithAnlpPrompt):
    PROMPT_VERSION = "0.2.1"
    DESCRIPTION = "与えられた選択肢の中から、最適な答えを選んでください。\n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choices = "\n".join([f"- {choice}" for choice in doc["choices"]["text"]])
        return f"質問:{q_doc_text}選択肢:\n{choices}\n回答:"


class FP2WithAlpacaPrompt(FP2WithAnlpPrompt):
    PROMPT_VERSION = 0.3
    DESCRIPTION = """以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

### 指示:
与えられた選択肢の中から、最適な答えを選んでください。

"""

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choices = "\n".join([f"- {choice}" for choice in doc["choices"]["text"]])
        input_text = f"{q_doc_text}" + f"出力は以下から選択してください：\n{choices}"
        return f"### 入力:\n{input_text}\n\n### 応答:\n"


class FP2WithRinnaInstructionSFT(FP2WithAnlpPrompt):
    PROMPT_VERSION = 0.4
    DESCRIPTION = "ユーザー: 与えられた選択肢の中から、最適な答えを選んでください。<NL>システム: 分かりました。<NL>"
    SEP = "<NL>"
    FEWSHOT_SEP = "<NL>"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"]
        if doc["context"] and doc["context"] != "":
            q_doc_text += "\n" + doc["context"]
        choices = self.SEP.join([f"- {choice}" for choice in doc["choices"]["text"]])
        input_text = f"質問：{q_doc_text}{self.SEP}" + f"選択肢：{self.SEP}{choices}"
        return f"ユーザー: {input_text}{self.SEP}システム: "


class FP2WithRinnaBilingualInstructionSFT(FP2WithRinnaInstructionSFT):
    PROMPT_VERSION = 0.5
    DESCRIPTION = "ユーザー: 与えられた選択肢の中から、最適な答えを選んでください。\nシステム: 分かりました。\n"
    SEP = "\n"
    FEWSHOT_SEP = "\n"


class FP2WithLlama2(FP2WithAnlpPrompt):
    PROMPT_VERSION = 0.6
    DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""
    SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT)
    DESCRIPTION = f"<s>[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n\n"
    INSTRUCTION = "与えられた選択肢の中から、最適な答えを選んでください。"
    FEWSHOT_SEP = " </s><s>[INST] "

    def doc_to_text(self, doc):
        q_doc_text = doc["question"]
        if doc["context"] and doc["context"] != "":
            q_doc_text += "\n" + doc["context"]
        choices = "\n".join([f"- {choice}" for choice in doc["choices"]["text"]])
        input_text = f"質問：{q_doc_text}" + f"出力は以下から選択してください：\n{choices}"
        return f"{self.INSTRUCTION}\n\n{input_text} [/INST] "


VERSIONS = [
    FP2WithAnlpPrompt,
    FP2WithAnlpPromptAlphabet,
    FP2WithFintanPrompt,
    FP2WithFintanPromptV1,
    FP2WithAlpacaPrompt,
    FP2WithRinnaInstructionSFT,
    FP2WithRinnaBilingualInstructionSFT,
    FP2WithLlama2,
]


def construct_tasks():
    tasks = {}
    for version_class in VERSIONS:
        tasks[
            f"fp2-{version_class.VERSION}-{version_class.PROMPT_VERSION}"
        ] = version_class
    tasks["fp2"] = FP2
    return tasks
