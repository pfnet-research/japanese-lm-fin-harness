import glob
import hashlib
import json
import os
from typing import Dict
from typing import List
from typing import Union
from typing import cast

from jlm_fin_eval.tasks import TaskManager


def get_task_set_dict() -> Dict[str, List[str]]:
    tasks = TaskManager().all_tasks
    task_prefix = set([task.split("-", 1)[0] for task in tasks])
    task_postfix = set(
        [
            ("-" + task.split("-", 1)[-1]) if len(task.split("-")) > 1 else ""
            for task in tasks
        ]
    )
    task_dict = dict(
        [
            (task_pre, list(filter(lambda x: x.startswith(task_pre), tasks)))
            for task_pre in task_prefix
        ]
    )
    task_set_dict = dict(
        [
            (
                postfix if postfix != "" else "-default",
                [
                    (
                        list(filter(lambda x: len(x.split("-")) == 1, _tasks))[0]
                        if postfix == ""
                        else sorted(
                            list(
                                filter(
                                    lambda x: "-" + x.split("-")[-1] in postfix,
                                    _tasks,
                                )
                            ),
                            key=lambda x: len(x),
                        )[-1]
                    )
                    for task_names, _tasks in task_dict.items()
                ],
            )
            for postfix in task_postfix
        ]
    )
    return task_set_dict


def get_model_settings() -> List[Dict[str, Union[str, int, List[str], bool]]]:
    model_setting_file_path = os.path.join(
        os.path.dirname(__file__), "models", "*.json"
    )
    model_setting_files = glob.glob(model_setting_file_path)
    model_settings: List[Dict[str, Union[str, int, List[str], bool]]] = []
    for model_setting_file in model_setting_files:
        with open(model_setting_file, "r") as f:
            setting_data = json.load(f)
        if isinstance(setting_data, list):
            model_settings.extend(setting_data)
        elif isinstance(setting_data, dict):
            model_settings.append(setting_data)
        else:
            raise ValueError(f"Invalid model setting file: {model_setting_file}")
    return model_settings


def main() -> None:
    model_settings = get_model_settings()
    task_sets_dict = get_task_set_dict()

    for model_setting in model_settings:
        model_name = cast(str, model_setting["model"])
        model_args = [f"pretrained={model_setting['model']}"]
        if "model_args" in model_setting:
            if len([x for x in model_setting["model_args"] if x.startswith("pretrained=")]) > 0:
                model_args = []
            model_args.extend(cast(List[str], model_setting["model_args"]))

        for task_version, tasks in task_sets_dict.items():
            task = ",".join(sorted(tasks))
            harness_command = f"""MODEL_ARGS="{','.join(model_args)}"
TASK="{task}"
python main.py --model {model_setting['run_type']} --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/{model_name}/result{task_version}.json"
# a100-80gb: {model_setting['a100-80gb']}
# a30-24gb: {model_setting['a30-24gb']}
# v100-32gb: {model_setting['v100-32gb']}
# v100-16gb: {model_setting['v100-16gb']}
"""
            save_path = os.path.join("models", model_name, f"harness{task_version}.sh")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, mode="w", encoding="utf-8") as f:
                f.writelines(harness_command)


if __name__ == "__main__":
    main()
