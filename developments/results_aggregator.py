import argparse
import glob
import json
from collections import defaultdict
from typing import Any
from typing import Dict
from typing import List


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
):
    best_metric_dict: Dict[str, Any] = defaultdict(
        lambda: {"metric_values": None, "n": -1, "key": ""}
    )  # Initialize best metric dict

    for prefix in prefix_list:
        json_files = glob.glob(
            f"{results_path}-*.json"
        )  # Read all json files with the given prefix
        for json_file in json_files:
            with open(json_file, "r") as f:
                data = json.load(f)  # Load the data

            for key, results in data["results"].items():
                base_keys = key.split("-")
                base_name = base_keys[0]

                metrics = metric_dict[base_name]

                # Set order for this key, if none specified, set it to "desc"
                _order_dict = order_dict.get(base_name, {})
                orders = [_order_dict.get(metric, "desc") for metric in metrics]

                metric_values = [results[metric] for metric in metrics]

                for i in range(len(metrics)):
                    if (
                        (best_metric_dict[base_name]["metric_values"] is None)
                        or (
                            orders[i] == "asc"
                            and metric_values[i]
                            < best_metric_dict[base_name]["metric_values"][i]
                        )
                        or (
                            orders[i] == "desc"
                            and metric_values[i]
                            > best_metric_dict[base_name]["metric_values"][i]
                        )
                    ):  # If the current performance metric is better than the best, update it
                        best_metric_dict[base_name]["metric_values"] = metric_values
                        best_metric_dict[base_name]["n"] = int(
                            json_file.split("-")[-1].split(".")[0]
                        )  # Get the index of the best score
                        best_metric_dict[base_name]["key"] = key
                        break
                    elif (
                        orders[i] == "asc"
                        and metric_values[i]
                        > best_metric_dict[base_name]["metric_values"][i]
                    ) or (
                        orders[i] == "desc"
                        and metric_values[i]
                        < best_metric_dict[base_name]["metric_values"][i]
                    ):
                        break

    return best_metric_dict


def main():
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

    print(f'TASK="{task}"')
    print(f'--num_fewshot "{num_fewshot}"')


if __name__ == "__main__":
    main()
