import argparse
import json
import os
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

    work_dir = str(run_settings["work_dir"])
    if work_dir == "":
        work_dir = os.getcwd()

    for model_setting in model_settings:
        model_name = cast(str, model_setting["model"])
        model_dir = os.path.join(work_dir, model_root_dir, model_name)

        result_json = os.path.join(model_dir, "result.json")
        harness_sh = os.path.join(model_dir, "harness.sh")

        if not os.path.exists(result_json) or not os.path.exists(harness_sh):
            continue

        result_data = json.load(open(result_json, "r"))
        final_results = {}
        for task, results in result_data["results"].items():
            task_name = task.split("-")[0]
            result = results.get("f1", results.get("acc"))
            final_results[task_name] = result
        with open(harness_sh, "r") as f:
            lines = f.readlines()
        estimated_result = [
            line for line in lines if line.startswith("# Estimated results: ")
        ][0]
        estimated_result = dict(
            [
                (result.split(":")[0], result.split(":")[1])
                for result in estimated_result.replace("# Estimated results: ", "")
                .strip()
                .split(",")
            ]
        )
        if (
            sum(
                [
                    result != final_results[task]
                    for task, result in estimated_result.items()
                ]
            )
            > 0
        ):
            print("=============")
            print(f"Model: {model_name}")
            print(f"Estimated results: {estimated_result}")
            print(f"Final results: {final_results}")


if __name__ == "__main__":
    main()
