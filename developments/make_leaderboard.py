import glob
import json
import os

result_dict = {}
prompt_dict = {}

for dir_name in glob.glob("models/*/*/"):
    _, company, modelname, _ = dir_name.split("/")
    company_model = company + "/" + modelname
    results_files = [
        x.replace("harness", "result").replace(".sh", ".json")
        for x in glob.glob(dir_name + "harness*.sh")
    ]
    if sum([not os.path.exists(x) for x in results_files]) > 0:
        print(f"Skipping {company_model} as results are not available")
        continue
    data = {}
    best_data = {}
    best_ave = 0.0
    for resuls_file in results_files:
        task_version = resuls_file.split("/")[-1].split("-", 1)[-1].replace(".json", "")
        with open(resuls_file, "r") as f:
            results_data = json.load(f)
            results_sum = 0
            count = 0
            tmp_result_dict = {}
            for task, results in results_data["results"].items():
                task_name = task.split("-")[0]
                result = results.get("f1,none", results.get("acc,none"))
                result = 100 * (result if result else 0)
                tmp_result_dict[task_name] = result
                if result:
                    results_sum += result
                    count += 1
            tmp_result_dict["Ave."] = results_sum / count if count > 0 else 0
            data[task_version] = tmp_result_dict
            if tmp_result_dict["Ave."] > best_ave:
                best_ave = tmp_result_dict["Ave."]
                best_data = tmp_result_dict
                prompt_dict[company_model] = task_version
    for task, result in best_data.items():
        result_dict.setdefault(company_model, {})[task] = result

sorted_results = sorted(
    result_dict.items(), key=lambda x: x[1].get("Ave.", 0), reverse=True
)

first_row = (
    "| Model | "
    + " | ".join(sorted(next(iter(result_dict.values()))))
    + " | prompt | \n| --- | "
    + " | ".join(["---"] * len(next(iter(result_dict.values()))))
    + " | --- |\n"
)
md_table = first_row
for company_model, results in sorted_results:
    md_table += (
        "| "
        + (
            "["
            if not (
                company_model.startswith("openai/")
                or company_model.startswith("gemini/")
                or company_model.startswith("anthropic/")
                or company_model.startswith("pfnet/plamo-1.0")
            )
            else ""
        )
        + company_model
        + (
            ("](https://huggingface.co/" + company_model.replace("/", "/") + ")")
            if not (
                company_model.startswith("openai/")
                or company_model.startswith("gemini/")
                or company_model.startswith("anthropic/")
            )
            else ""
        )
        + " | "
        + "{:.2f}".format(results.pop("Ave."))
        + " | "
        + " | ".join(
            (
                "{:.2f}".format(results.get(task_name, "N/A"))
                if not isinstance(results.get(task_name, "N/A"), str)
                else results.get(task_name, "N/A")
            )
            for task_name in sorted(results)
        )
        + f" | {prompt_dict[company_model]} |\n"
    )

with open("README.md", "r") as f:
    readme_content = f.read()

start_index = readme_content.index("<!-- lb start -->") + len("<!-- lb start -->")
end_index = readme_content.index("<!-- lb end -->")
new_readme_content = (
    readme_content[:start_index] + "\n" + md_table + readme_content[end_index:]
)

with open("README.md", "w") as f:
    f.write(new_readme_content)

print("Leader Board was written in README.md")
