import json
import glob

result_dict = {}

for file_name in glob.glob("models/*/*/result.json"):
    _, company, modelname, _ = file_name.split("/")
    company_model = company + "/" + modelname
    with open(file_name, 'r') as f:
        data = json.load(f)
    results_sum = 0
    count = 0
    for task, results in data["results"].items():
        task_name = task.split('-')[0]
        result = results.get("f1", results.get("acc"))
        result = 100 * (result if result else 0)
        result_dict.setdefault(company_model, {})[task_name] = result
        if result:
            results_sum += result
            count += 1
    result_dict.setdefault(company_model, {})['Ave.'] = results_sum / count if count > 0 else 0

sorted_results = sorted(result_dict.items(), key=lambda x: x[1].get('Ave.', 0), reverse=True)

first_row = "| Model | " + ' | '.join(sorted(next(iter(result_dict.values())))) + " |\n| --- | --- | " + ' | '.join(['---'] * len(next(iter(result_dict.values())))) + " |\n"
md_table = first_row
for company_model, results in sorted_results:
    md_table += "| [" + company_model + "](https://huggingface.co/" + company_model.replace("/", "/") + ") | " + "{:.2f}".format(results.pop('Ave.')) + " | " + ' | '.join("{:.2f}".format(results.get(task_name, "N/A")) for task_name in sorted(results)) + " |\n"

with open("README.md", "r") as f:
    readme_content = f.read()

start_index = readme_content.index("<!-- lb start -->") + len("<!-- lb start -->")
end_index = readme_content.index("<!-- lb end -->")
new_readme_content = readme_content[:start_index] + "\n" + md_table + readme_content[end_index:]

with open("README.md", "w") as f:
    f.write(new_readme_content)

print("Leader Board was written in README.md")
