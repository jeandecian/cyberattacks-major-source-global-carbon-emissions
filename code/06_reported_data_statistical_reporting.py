import constants as c
import file_utils as f
import latex_utils as l
import pandas as pd
import statistic_utils as s

reported_file_name = "500T-one-tailed-p-wilcoxon"
statistics = []

for path in f.get_all_files_recursively(c.REPORTED_DATA_DIRECTORY_PATH):
    if f.get_file_extension(path) != c.EXTENSION_CSV:
        continue

    if f.get_file_name(path) == f"{reported_file_name}.csv":
        continue

    df = f.get_dataframe_from_csv(path)
    wilcoxon_stat, one_tailed_p_wilcoxon = s.perform_wilcoxon_signed_rank_test(df, 2, 3)

    path = path.split(".")[0]
    path_elements = path.split("-")

    attack_type = ""

    metric_index = 2
    if path_elements[1] == "denial":
        attack_type = "-".join(path_elements[1:4])
        metric_index += 2
    else:
        attack_type = path_elements[1]

    metric = "-".join(path_elements[metric_index:])

    statistics.append(
        s.format_statistics(
            c.REPORTED_METRICS_NAME.get(metric, metric).replace(
                "Power", "Power Consumption"
            ),
            c.ATTACK_TYPES.get(attack_type, attack_type),
            df.shape[0],
            wilcoxon_stat,
            one_tailed_p_wilcoxon,
        )
    )

headers = (
    "Metric",
    c.ATTACK_TYPE,
    "n",
    "Wilcoxon Statistic $W$",
    "P-Value",
    "Significance ($\\alpha=0.05$)",
)
summary_df = pd.DataFrame(statistics, columns=headers).sort_values(
    by=["Metric", c.ATTACK_TYPE], ascending=True
)
summary_df[list(headers[3:5])] = summary_df[list(headers[3:5])].astype(float)

latex_table = l.generate_statistical_table(headers, summary_df)

f.save_dataframe_as_csv(
    f"{c.REPORTED_DATA_DIRECTORY_PATH}/{reported_file_name}.csv", summary_df
)
f.save_file(f"{c.TABLES_OUTPUT_DIRECTORY_PATH}/{reported_file_name}.tex", latex_table)
