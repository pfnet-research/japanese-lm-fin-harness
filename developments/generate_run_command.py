import argparse
import glob
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

        sh_files = glob.glob(os.path.join(model_dir, "harness*.sh"))
        sh_file_names = [os.path.basename(f) for f in sh_files]
        results_files = [
            os.path.join(
                model_dir, result.replace("harnsee", "result").replace(".sh", ".json")
            )
            for result in sh_file_names
        ]

        if sum([not os.path.exists(result_json) for result_json in results_files]) == 0:
            continue

        command = (
            cast(str, run_settings["preprocess_harness"])
            + f"ls {model_dir} | xargs -I [] poetry run bash {model_dir}/[]"
            + cast(str, run_settings["postprocess_harness"])
        )
        command = (
            command.replace(
                "${model_name}",
                cast(str, model_setting["model"]).split("/")[-1],
            )
            .replace("${n_gpu}", str(model_setting["n_gpu"]))
            .replace("${memory}", str(model_setting["memory_Gi"]))
            .replace("${gpu_request}", str(model_setting["gpu_request"]))
            .replace("${env}", env_var_str)
            .replace("${work_dir}", work_dir)
            .replace("${repo}", cast(str, model_setting["model"]))
        )
        commands.append(command)
    print("\n".join(commands))


if __name__ == "__main__":
    main()
