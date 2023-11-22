import argparse
import json
import os
from typing import Dict
from typing import cast

from developments.make_run_commands import get_model_settings


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute the best metrics")
    parser.add_argument(
        "--model_dir",
        type=str,
        default="models",
        help="Path to the model dir for harness.sh",
    )
    model_root_dir = parser.parse_args().model_dir
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
    work_dir = str(run_settings["work_dir"])
    if work_dir == "":
        work_dir = os.getcwd()

    for model_setting in model_settings:
        model_name = cast(str, model_setting["model"])
        model_dir = os.path.join(work_dir, model_root_dir, model_name)

        result_json = os.path.join(model_dir, "results.json")
        harness_sh = os.path.join(model_dir, "harness.sh")

        if not os.path.exists(harness_sh):
            continue
        if os.path.exists(result_json):
            continue

        command = (
            cast(str, run_settings["preprocess_harness"])
            + f"poetry run bash {harness_sh}"
            + cast(str, run_settings["postprocess_harness"])
        )
        command = (
            command.replace(
                "${model_name}",
                cast(str, model_setting["model"]).split("/")[-1],
            )
            .replace("${n_gpu}", str(model_setting["n_gpu"]))
            .replace("${memory}", str(model_setting["memory_Gi"]))
            .replace("${gpu_vram}", str(model_setting["gpu_vram_gb"]))
            .replace("${env}", env_var_str)
            .replace("${work_dir}", work_dir)
            .replace("${repo}", cast(str, model_setting["model"]))
        )
        commands.append(command)
    print("\n".join(commands))


if __name__ == "__main__":
    main()
