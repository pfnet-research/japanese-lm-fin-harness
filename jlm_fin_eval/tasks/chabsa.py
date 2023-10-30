import inspect
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
    VERSION = 1
    DATASET_PATH = inspect.getfile(jlm_fin_eval.datasets.chabsa.chabsa)
    DATASET_NAME = "chABSA"

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
        doc_text = "以下のセンテンスにおける、ターゲットのセンチメントをpositiveかnegativeで答えてください。\n\n"
        doc_text += f"センテンス: {doc['sentence']}\n"
        doc_text += f"ターゲット: {doc['target']}\n"
        doc_text += "回答:"
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
        gold = doc["answer"]

        out = {
            "acc": (
                results,
                gold,
            ),
            "f1": (
                results,
                gold,
            ),
        }
        return out

    def higher_is_better(self):
        return {"acc": True, "f1": True}

    def aggregation(self):
        return {
            "exact_match": partial(self._chabsa_agg, "exact_match"),
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
