import glob
import json
import os.path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

result_dict = {}

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for file_name in glob.glob("models/*/*/result.json", root_dir=root_path):
    _, company, modelname, _ = file_name.split("/")
    company_model = company + "/" + modelname
    with open(file_name, "r") as f:
        data = json.load(f)
    results_sum = 0
    count = 0
    for task, results in data["results"].items():
        task_name = task.split("-")[0]
        result = results.get("f1", results.get("acc"))
        result = 100 * (result if result else 0)
        result_dict.setdefault(company_model, {})[task_name] = result
        if result:
            results_sum += result
            count += 1
    result_dict.setdefault(company_model, {})["Ave."] = (
        results_sum / count if count > 0 else 0
    )

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["chabsa"], result_dict.values())))


def curv(x, a, b, c):
    return c * (1 - np.exp(a * (x - b)))


popt, pocv = curve_fit(curv, average, target, p0=[-0.1, 30, 95])
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
    label=f"${popt[2]:0.2f} "
    + "\\times"
    + " (1 - \\exp{("
    + f"{popt[0]:0.2f}"
    + " \\times (x - "
    + f"{popt[1]:0.2f}"
    + "))})$\n$R^2="
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


def curv(x, a, b):
    return a * (x - b)


popt, pocv = curve_fit(curv, average, target, p0=[1, 0])
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
    label=f"${popt[0]:0.2f} (x - {popt[1]:0.2f})$\n$R^2=" + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("cma_basics")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-cma_basics.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["cpa_audit"], result_dict.values())))


def curv(x, a, b):
    return a * (x - b)


popt, pocv = curve_fit(curv, average, target, p0=[1, 0])
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
    label=f"${popt[0]:0.2f} (x - {popt[1]:0.2f})$\n$R^2=" + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("cpa_audit")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-cpa_audit.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["fp2"], result_dict.values())))


def curv(x, a, b):
    return a * (x - b)


popt, pocv = curve_fit(curv, average, target, p0=[1, 0])
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
    label=f"${popt[0]:0.2f} (x - {popt[1]:0.2f})$\n$R^2=" + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("fp2")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-fp2.png")
plt.savefig(save_file_path)
plt.close()

average = np.array(list(map(lambda x: x["Ave."], result_dict.values())))
target = np.array(list(map(lambda x: x["security_sales_1"], result_dict.values())))


def curv(x, a, b):
    return a * (x - b)


popt, pocv = curve_fit(curv, average, target, p0=[1, 0])
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
    label=f"${popt[0]:0.2f} (x + {-popt[1]:0.2f})$\n$R^2=" + f"{r_squared:0.2f}$",
)
plt.xlabel("Ave.")
plt.ylabel("security_sales_1")
plt.legend()
save_file_path = os.path.join(root_path, "analysis", "figs", "ave-security_sales_1.png")
plt.savefig(save_file_path)
