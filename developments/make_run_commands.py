import glob
import hashlib
import json
import os
import warnings
from typing import Dict
from typing import List
from typing import Union
from typing import cast

import jlm_fin_eval.tasks


def get_task_sets() -> List[List[str]]:
    tasks = list(jlm_fin_eval.tasks.TASK_REGISTRY.keys())
    task_prefix = set([task.split("-", 1)[0] for task in tasks])
    task_dict = dict(
        [
            (task_pre, list(filter(lambda x: x.startswith(task_pre), tasks)))
            for task_pre in task_prefix
        ]
    )
    task_max_len = max([len(task) for task in task_dict.values()])
    task_temp = [
        value + value[:1] * (task_max_len - len(value))
        for _, value in task_dict.items()
    ]
    task_sets = list(zip(*task_temp))
    return task_sets


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
    task_sets = get_task_sets()
    model_settings = get_model_settings()
    run_setting_file = os.path.join(
        os.path.dirname(__file__), "run_settings", "settings.json"
    )
    run_settings = {
        "env_var": {},
        "preprocess": "",
        "postprocess": "",
    }
    if os.path.exists(run_setting_file):
        with open(run_setting_file, "r") as f:
            run_settings.update(json.load(f))

    commands = []
    for env_var_name, env_var_value in cast(
        Dict[str, str], run_settings["env_var"]
    ).items():
        commands.append(f"export {env_var_name}={env_var_value}")

    env_var_str = "".join([command + ";" for command in commands])

    for model_setting in model_settings:
        for n_fewshot in range(5):
            for task in task_sets:
                try:
                    model_args = [f"pretrained={model_setting['model']}"]
                    if "model_args" in model_setting:
                        model_args.extend(cast(List[str], model_setting["model_args"]))
                    task_hash = hashlib.sha256(
                        "".join(task).encode("utf-8")
                    ).hexdigest()[-8:]
                    work_dir = str(run_settings["work_dir"])
                    if work_dir == "":
                        work_dir = os.getcwd()
                    command = (
                        cast(str, run_settings["preprocess"])
                        + f"poetry run python main.py --model hf --model_args {','.join(model_args)} --task {','.join(task)} --output_path results/{model_setting['model']}-{n_fewshot}-{task_hash}.json"
                        + cast(str, run_settings["postprocess"])
                    )
                    command = (
                        command.replace(
                            "${model_name}",
                            cast(str, model_setting["model"]).split("/")[-1],
                        )
                        .replace("${n_fewshot}", str(n_fewshot))
                        .replace("${n_gpu}", str(model_setting["n_gpu"]))
                        .replace("${memory}", str(model_setting["memory_Gi"]))
                        .replace("${gpu_vram}", str(model_setting["gpu_vram_gb"]))
                        .replace("${env}", env_var_str)
                        .replace("${work_dir}", work_dir)
                        .replace("${task_hash}", task_hash)
                        .replace("${repo}", cast(str, model_setting["model"]))
                    )
                    commands.append(command)
                except Exception as e:
                    warnings.warn(str(model_setting))
                    raise e
    print("\n".join(commands))


if __name__ == "__main__":
    main()
