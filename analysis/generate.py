import glob
import json
import os.path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

result_dict = {}

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    for task, result in best_data.items():
        result_dict.setdefault(company_model, {})[task] = result

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["chabsa"], result_dict.values())))


def curv(x, a, b, range_min, range_max):
    return (range_max - range_min) / (1 + np.exp(-a * (x - b))) + range_min


popt, pocv = curve_fit(curv, average, target, p0=[-0.1, 30, 100, 20])
residuals = target - curv(average, *popt)
rss = np.sum(residuals**2)
tss = np.sum((target - np.mean(target)) ** 2)
r_squared = 1 - (rss / tss)
dummy_x = np.arange(min(average), max(average), 1)
dummy_y = curv(dummy_x, *popt)
plt.scatter(average, target)
plt.plot(
    dummy_x,
    dummy_y,
    label=f"$({popt[2]:0.2f} - {popt[3]:0.2f}) "
    + "\\times (1 + \\exp{("
    + f"{-popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))}) + "
    + f"{popt[3]:0.2f}$\n$R^2="
    + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("chabsa")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-chabsa.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["cma_basics"], result_dict.values())))


def curv(x, a, b, range_min, range_max):
    return (range_max - range_min) / (1 + np.exp(-a * (x - b))) + range_min


popt, pocv = curve_fit(curv, average, target, p0=[0.1, 20, 100, 20])
residuals = target - curv(average, *popt)
rss = np.sum(residuals**2)
tss = np.sum((target - np.mean(target)) ** 2)
r_squared = 1 - (rss / tss)
dummy_x = np.arange(min(average), max(average), 1)
dummy_y = curv(dummy_x, *popt)
plt.scatter(average, target)
plt.plot(
    dummy_x,
    dummy_y,
    label=f"$({popt[2]:0.2f} - {popt[3]:0.2f}) "
    + "\\times (1 + \\exp{("
    + f"{-popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))}) + "
    + f"{popt[3]:0.2f}$\n$R^2="
    + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("cma_basics")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-cma_basics.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["cpa_audit"], result_dict.values())))


def curv(x, a, b, range_min, range_max):
    return (range_max - range_min) / (1 + np.exp(-a * (x - b))) + range_min


popt, pocv = curve_fit(curv, average, target, p0=[0.1, 70, 100, 20])
residuals = target - curv(average, *popt)
rss = np.sum(residuals**2)
tss = np.sum((target - np.mean(target)) ** 2)
r_squared = 1 - (rss / tss)
dummy_x = np.arange(min(average), max(average), 1)
dummy_y = curv(dummy_x, *popt)
plt.scatter(average, target)
plt.plot(
    dummy_x,
    dummy_y,
    label=f"$({popt[2]:0.2f} - {popt[3]:0.2f}) "
    + "\\times (1 + \\exp{("
    + f"{-popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))}) + "
    + f"{popt[3]:0.2f}$\n$R^2="
    + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("cpa_audit")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-cpa_audit.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["fp2"], result_dict.values())))


def curv(x, a, b, range_min, range_max):
    return (range_max - range_min) / (1 + np.exp(-a * (x - b))) + range_min


popt, pocv = curve_fit(curv, average, target, p0=[0.2, 70, 100, 20])
residuals = target - curv(average, *popt)
rss = np.sum(residuals**2)
tss = np.sum((target - np.mean(target)) ** 2)
r_squared = 1 - (rss / tss)
dummy_x = np.arange(min(average), max(average), 1)
dummy_y = curv(dummy_x, *popt)
plt.scatter(average, target)
plt.plot(
    dummy_x,
    dummy_y,
    label=f"$({popt[2]:0.2f} - {popt[3]:0.2f}) "
    + "\\times (1 + \\exp{("
    + f"{-popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))}) + "
    + f"{popt[3]:0.2f}$\n$R^2="
    + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("fp2")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-fp2.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["security_sales_1"], result_dict.values())))


def curv(x, a, b, range_min, range_max):
    return (range_max - range_min) / (1 + np.exp(-a * (x - b))) + range_min


popt, pocv = curve_fit(curv, average, target, p0=[0.1, 20, 100, 20])
residuals = target - curv(average, *popt)
rss = np.sum(residuals**2)
tss = np.sum((target - np.mean(target)) ** 2)
r_squared = 1 - (rss / tss)
dummy_x = np.arange(min(average), max(average), 1)
dummy_y = curv(dummy_x, *popt)
plt.scatter(average, target)
plt.plot(
    dummy_x,
    dummy_y,
    label=f"$({popt[2]:0.2f} - {popt[3]:0.2f}) "
    + "\\times (1 + \\exp{("
    + f"{-popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))}) + "
    + f"{popt[3]:0.2f}$\n$R^2="
    + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("security_sales_1")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-security_sales_1.png")
plt.savefig(save_file_path)
