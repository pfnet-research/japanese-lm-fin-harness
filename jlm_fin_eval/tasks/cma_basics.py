import inspect

import numpy as np
from lm_eval.base import MultipleChoiceTask
from lm_eval.base import mean
from lm_eval.base import rf
from sklearn.metrics import accuracy_score

import jlm_fin_eval.datasets.cma_basics.cma_basics


class CmaBasics(MultipleChoiceTask):
    VERSION = 1.0
    DATASET_PATH = inspect.getfile(jlm_fin_eval.datasets.cma_basics.cma_basics)
    DATASET_NAME = "cma_basics"
    DESCRIPTION = "[問題]に対する[答え]を[選択肢]の中から選んでください。\n\n"

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
        doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            doc_text += doc["context"] + "\n"
        doc_text += "\n【選択肢】\n"
        for choice_id, choice_text in zip(doc["choices"]["id"], doc["choices"]["text"]):
            doc_text += chr(choice_id + 65) + ": " + choice_text + "\n"
        doc_text += "\n【答え】\n"
        # doc_text += chr(int(doc["answer"]) + 65)
        return doc_text

    def doc_to_target(self, doc):
        answer = chr(int(doc["answer"]) + 65)
        return answer

    @staticmethod
    def compute_scores(gold, pred):
        acc = accuracy_score(gold, pred)

        return {"acc": acc}

    def construct_requests(self, doc, ctx):
        lls = [
            rf.loglikelihood(ctx, chr(choice + 65))[0]
            for choice in doc["choices"]["id"]
        ]

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


class CmaBasicsWithAnlpPrompt(CmaBasics):
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


class CmaBasicsWithAnlpPromptAlphabet(CmaBasics):
    PROMPT_VERSION = "0.1.2"
    DESCRIPTION = "[問題]に対する[答え]を[選択肢]の中からアルファベットで選んでください。\n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choice_doc_text = []
        for choice_id, choice_text in zip(doc["choices"]["id"], doc["choices"]["text"]):
            choice_doc_text.append(chr(choice_id + 65) + ":" + choice_text)
        return f"[問題]:{q_doc_text}[選択肢]:[{', '.join(doc['choices']['text'])}]\n[答え]:"


class CmaBasicsWithFintanPrompt(CmaBasics):
    PROMPT_VERSION = 0.2
    DESCRIPTION = (
        "質問と回答の選択肢を入力として受け取り、選択肢から回答を選択してください。なお、回答は選択肢の番号(例:0)でするものとします。 \n\n"
    )

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


class CmaBasicsWithFintanPromptV1(CmaBasicsWithAnlpPrompt):
    PROMPT_VERSION = "0.2.1"
    DESCRIPTION = "与えられた選択肢の中から、最適な答えを選んでください。 \n\n"

    def doc_to_text(self, doc):
        q_doc_text = doc["question"] + "\n"
        if doc["context"] and doc["context"] != "":
            q_doc_text += doc["context"] + "\n"
        choices = "\n".join([f"- {choice}" for choice in doc["choices"]["text"]])
        return f"質問:{q_doc_text}" f"選択肢:{choices}\n" "回答:"


VERSIONS = [
    CmaBasicsWithAnlpPrompt,
    CmaBasicsWithAnlpPromptAlphabet,
    CmaBasicsWithFintanPrompt,
    CmaBasicsWithFintanPromptV1,
    # CmaBasicsWithAlpacaPrompt,
    # CmaBasicsWithRinnaInstructionSFT,
    # CmaBasicsWithRinnaBilingualInstructionSFT,
    # CmaBasicsWithLlama2,
]


def construct_tasks():
    tasks = {}
    for version_class in VERSIONS:
        tasks[
            f"cma_basics-{version_class.VERSION}-{version_class.PROMPT_VERSION}"
        ] = version_class
    tasks["cma_basics"] = CmaBasics
    return tasks
