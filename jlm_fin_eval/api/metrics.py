from typing import Tuple

import numpy as np
from lm_eval.api.registry import register_aggregation
from lm_eval.api.registry import register_metric
from sklearn.metrics import f1_score


@register_aggregation("macro_f1_score")
def macro_f1_score(items: Tuple) -> float | np.ndarray:
    unzipped_list = list(zip(*items))
    golds = unzipped_list[0]
    preds = unzipped_list[1]
    fscore = f1_score(golds, preds, average="macro")
    return fscore


@register_aggregation("2class_adjusted_macro_f1_score_for_chabsa")
def two_class_adjusted_macro_f1_score_for_chabsa(items: Tuple) -> float | np.ndarray:
    unzipped_list = list(zip(*items))
    golds = unzipped_list[0]
    preds = unzipped_list[1]
    fscore = f1_score(golds, preds, average="macro") * 1.5
    return fscore
