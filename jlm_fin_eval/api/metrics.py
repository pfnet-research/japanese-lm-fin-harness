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


@register_metric(
    metric="f1_norm",
    higher_is_better=True,
    output_type="multiple_choice",
)
def f1_norm_fn(items):  # This is a passthrough function
    return items


@register_metric(
    metric="map",
    higher_is_better=True,
    output_type="multiple_choice",
)
def map_fn(items):  # This is a passthrough function
    return items


@register_metric(
    metric="map_2",
    higher_is_better=True,
    output_type="multiple_choice",
)
def map_2_fn(items):  # This is a passthrough function
    return items


@register_metric(
    metric="map_3",
    higher_is_better=True,
    output_type="multiple_choice",
)
def map_3_fn(items):  # This is a passthrough function
    return items


@register_metric(
    metric="map_4",
    higher_is_better=True,
    output_type="multiple_choice",
)
def map_4_fn(items):  # This is a passthrough function
    return items
