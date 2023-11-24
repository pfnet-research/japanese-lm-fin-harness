import argparse
import hashlib
import json
import os
from collections import defaultdict
from typing import Any
from typing import Dict
from typing import List
from typing import Union
from typing import cast

from developments.make_run_commands import get_model_settings
from developments.make_run_commands import get_task_sets


def get_best_metric(
    json_files: List[str],
    prefix_list: List[str] = [
        "chabsa",
        "cma_basics",
        "cpa_audit",
        "security_sales_1",
        "fp2",
    ],
    metric_dict: Dict[str, List[str]] = {
        "chabsa": ["f1", "acc"],
        "cma_basics": ["acc", "map", "map_2", "map_3", "map_4"],
        "cpa_audit": ["acc", "map", "map_2", "map_3", "map_4"],
        "security_sales_1": ["acc", "map", "map_2", "map_3", "map_4"],
        "fp2": ["acc", "map", "map_2", "map_3", "map_4"],
    },
    order_dict: Dict[str, Dict[str, str]] = {},
) -> Dict:
    best_metric_dict: Dict[str, Any] = defaultdict(
        lambda: {"metric_values": None, "n": -1, "key": ""}
    )  # Initialize best metric dict
    results_data: Dict[
        str, List[Dict[str, Union[int, str, Dict[str, float]]]]
    ] = defaultdict(list)
    for json_file in json_files:
        with open(json_file, "r") as f:
            data = json.load(f)  # Load the data
        for (key, results), few_shot in zip(
            cast(Dict[str, Dict[str, float]], data["results"]).items(),
            cast(List[int], data["config"]["num_fewshot"]),
        ):
            base_keys = key.split("-")
            base_name = base_keys[0]
            if base_name not in prefix_list:
                continue
            results_data[base_name].append(
                {"num_few_shot": few_shot, "results": results, "key": key}
            )

    for prefix in prefix_list:
        target_data: List[Dict[str, Union[int, str, Dict[str, float]]]] = results_data[
            prefix
        ]
        metrics = metric_dict[prefix]
        orders = [order_dict.get(metric, "desc") for metric in metrics]
        target_data = sorted(
            target_data,
            key=lambda x: [
                cast(Dict[str, float], x["results"])[metric]
                * (-1.0 if order == "asc" else 1.0)
                for metric, order in zip(metrics, orders)
            ],
            reverse=True,
        )
        best_metric_dict[prefix]["metric_values"] = cast(
            Dict[str, float], target_data[0]["results"]
        )[metrics[0]]
        best_metric_dict[prefix]["n"] = target_data[0]["num_few_shot"]
        best_metric_dict[prefix]["key"] = target_data[0]["key"]

    return best_metric_dict


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute the best metrics")
    parser.add_argument(
        "--results_path",
        type=str,
        default="results",
        help="Path to the results",
    )
    parser.add_argument(
        "--outputs_path",
        type=str,
        default="models",
        help="Path to the results",
    )
    args = parser.parse_args()

    model_settings = get_model_settings()
    task_sets: List[List[str]] = get_task_sets()
    task_hashes: List[str] = [
        hashlib.sha256("".join(task).encode("utf-8")).hexdigest()[-8:]
        for task in task_sets
    ]

    for model_setting in model_settings:
        model_name = cast(str, model_setting["model"])
        json_files: List[str] = sum(
            [
                [
                    os.path.join(
                        args.results_path, f"{model_name}-{n_fewshot}-{task_hash}.json"
                    )
                    for task_hash in task_hashes
                ]
                for n_fewshot in range(5)
            ],
            [],
        )
        has_missing = False
        for json_file in json_files:
            if not os.path.exists(json_file):
                has_missing = True
                print(f"{json_file} is missing")
        if has_missing:
            continue

        best_metrics = get_best_metric(json_files=json_files)
        os.makedirs(os.path.join(args.outputs_path, model_name), exist_ok=True)

        model_args = [f"pretrained={model_setting['model']}"]
        if "model_args" in model_setting:
            model_args.extend(cast(List[str], model_setting["model_args"]))
        task = ",".join([str(values["key"]) for _, values in best_metrics.items()])
        num_fewshots = ",".join(
            [str(values["n"]) for _, values in best_metrics.items()]
        )
        values = ",".join(
            [
                prefix + ":" + str(values["metric_values"])
                for prefix, values in best_metrics.items()
            ]
        )
        harness_command = f"""MODEL_ARGS="{','.join(model_args)}"
TASK="{task}"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "{num_fewshots}" --device "cuda" --output_path "models/{model_name}/result.json"
# Estimated results: {values}
"""
        save_path = os.path.join(args.outputs_path, model_name, "harness.sh")
        with open(save_path, mode="w", encoding="utf-8") as f:
            f.writelines(harness_command)


if __name__ == "__main__":
    main()
