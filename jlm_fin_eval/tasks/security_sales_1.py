import inspect

import numpy as np
from lm_eval.base import MultipleChoiceTask
from lm_eval.base import mean
from lm_eval.base import rf
from sklearn.metrics import accuracy_score

import jlm_fin_eval.datasets.security_sales_1.security_sales_1


class SecuritySales1(MultipleChoiceTask):
    VERSION = 1
    DATASET_PATH = inspect.getfile(
        jlm_fin_eval.datasets.security_sales_1.security_sales_1
    )
    DATASET_NAME = "security_sales_1"

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
    def get_answer(doc):
        return chr(int(doc["answer"]) + 65)

    @staticmethod
    def compute_scores(gold, pred):
        acc = accuracy_score(gold, pred)

        return {"acc": acc}

    def construct_requests(self, doc, ctx):
        lls = [
            rf.loglikelihood(ctx, "{}".format(chr(choice + 65)))[0]
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
