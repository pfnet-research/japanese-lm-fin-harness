import inspect

from lm_eval.base import Task

import jlm_fin_eval.datasets.cma_basics.cma_basics


class CmaBasics(Task):
    VERSION = 1
    DATASET_PATH = inspect.getfile(jlm_fin_eval.datasets.cma_basics.cma_basics)
