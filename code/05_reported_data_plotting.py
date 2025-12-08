import constants as c
import file_utils as f
import plot_utils as p

metric_dfs = {}

for metric in c.REPORTED_METRICS:
    if "Power" in metric:
        metric = metric.replace("Power", "Power Consumption")

    metric_dfs[f"{metric.lower().split(' (')[0].replace(' ', '-')}"] = {
        "name": metric,
        "dfs": [],
    }

paths = f.get_all_files_recursively(f"{c.REPORTED_DATA_DIRECTORY_PATH}")

for path in paths:
    if f.get_file_extension(path) != c.EXTENSION_CSV:
        continue

    df = f.get_dataframe_from_csv(path)

    for attack in c.ATTACK_TYPES.keys():
        if attack not in path:
            continue

        path = path.split(f"{attack}-")[-1].split(".")[0]

    metric_dfs[path].get("dfs").append(df)

for metric in metric_dfs:
    p.plot_scatters_per_metric(
        metric_dfs[metric].get("dfs"), metric_dfs[metric].get("name")
    )
