import argparse
import glob
import json
from collections import defaultdict
from typing import Any
from typing import Dict
from typing import List
from typing import Union
from typing import cast


def get_best_metric(
    results_path: str = "results/gpt-neox-japanese",
    prefix_list: List[str] = ["chabsa", "cma_basics", "cpa", "security_sales_1"],
    metric_dict: Dict[str, List[str]] = {
        "chabsa": ["f1", "acc"],
        "cma_basics": ["acc", "map", "map_2", "map_3", "map_4"],
        "cpa": ["acc", "map", "map_2", "map_3", "map_4"],
        "security_sales_1": ["acc", "map", "map_2", "map_3", "map_4"],
    },
    order_dict: Dict[str, Dict[str, str]] = {},
) -> Dict:
    best_metric_dict: Dict[str, Any] = defaultdict(
        lambda: {"metric_values": None, "n": -1, "key": ""}
    )  # Initialize best metric dict
    results_data: Dict[
        str, List[Dict[str, Union[int, str, Dict[str, float]]]]
    ] = defaultdict(list)
    json_files = [f"{results_path}-{i}.json" for i in range(5)]
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
        default="results/gpt-neox-japanese",
        help="Path to the results",
    )
    parser.add_argument(
        "--prefix_list",
        type=str,
        default="chabsa,cma_basics,cpa,security_sales_1",
        help="The list of prefixes",
    )
    args = parser.parse_args()

    prefix_list: List[str] = args.prefix_list.split(",")

    best_metrics = get_best_metric(
        results_path=args.results_path, prefix_list=prefix_list
    )

    # Parse best metrics into output format
    task = ",".join([str(best_metrics[prefix]["key"]) for prefix in prefix_list])
    num_fewshot = ",".join([str(best_metrics[prefix]["n"]) for prefix in prefix_list])
    values = ",".join(
        [str(best_metrics[prefix]["metric_values"]) for prefix in prefix_list]
    )

    print(f'TASK="{task}"')
    print(f'--num_fewshot "{num_fewshot}"')
    print(f"{values}")


if __name__ == "__main__":
    main()
