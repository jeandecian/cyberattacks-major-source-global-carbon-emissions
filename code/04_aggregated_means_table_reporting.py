import constants as c
import file_utils as f
import latex_utils as l

df = f.get_dataframe_from_csv(f"{c.PROCESSED_DATA_DIRECTORY_PATH}/aggregated/means.csv")

for attack_id, attack_type in c.ATTACK_TYPES.items():
    for metric_column in c.REPORTED_METRICS:
        attack_type_condition = df[c.ATTACK_TYPE] == attack_type
        reported_columns = c.ORDERED_HEADERS[:3] + [metric_column]

        idle_df = df[attack_type_condition & (df[c.MODE] == c.ATTACK_MODES[0])][
            reported_columns
        ]

        attack_df = df[attack_type_condition & (df[c.MODE] == c.ATTACK_MODES[1])][
            reported_columns
        ]
        idle_attack_df = idle_df.merge(
            attack_df, on=[c.ATTACK, c.HOST, c.RUN], how="outer"
        )

        idle_label = f"Base {metric_column.split()[-1].split('_')[0]}"
        attack_label = f"Attack {metric_column.split()[-1].split('_')[0]}"

        idle_attack_df.rename(
            columns={
                f"{metric_column}_x": idle_label,
                f"{metric_column}_y": attack_label,
            },
            inplace=True,
        )

        if attack_type == "Cryptojacking":
            coinimp_zenbook_idle = idle_attack_df.loc[
                (idle_attack_df[c.ATTACK] == "CoinIMP (CPU) (0%)")
                & (idle_attack_df[c.HOST] == c.HOST_NAMES.get("zenbook")),
                idle_label,
            ].iloc[0]

            for percent in (10, 20, 30, 40, 50, 100):
                idle_attack_df.loc[
                    (idle_attack_df[c.ATTACK] == f"CoinIMP (CPU) ({percent}%)")
                    & (idle_attack_df[c.HOST] == c.HOST_NAMES.get("zenbook")),
                    idle_label,
                ] = coinimp_zenbook_idle

        if "GPU" in metric_column:
            idle_attack_df = idle_attack_df[
                idle_attack_df[c.ATTACK].str.contains("GPU")
            ]

        idle_attack_df.loc[idle_attack_df[idle_label] == 0, idle_label] = 0.1
        idle_attack_df["Variation (%)"] = (
            (idle_attack_df[attack_label] - idle_attack_df[idle_label])
            / idle_attack_df[idle_label]
            * 100
        ).round(2)

        idle_attack_df[c.ATTACK] = [
            c.REPORTED_ATTACKS.get(attack, attack)
            for attack in idle_attack_df[c.ATTACK]
        ]
        idle_attack_df.rename(columns={c.ATTACK: c.STUDY}, inplace=True)

        idle_attack_df[c.HOST] = [
            c.REPORTED_HOSTS.get(host, host) for host in idle_attack_df[c.HOST]
        ]

        idle_attack_df.dropna(inplace=True)

        if len(idle_attack_df) == 0:
            continue

        idle_attack_df = idle_attack_df.sort_values(
            by=[c.STUDY, c.HOST, c.RUN], ascending=True
        )
        idle_attack_df.drop(columns=[c.RUN], inplace=True)

        latex_table = l.generate_attack_metric_table(
            attack_type, metric_column, idle_attack_df
        )

        if "Power" in metric_column:
            metric_column = metric_column.replace("Power", "Power Consumption")

        reported_file_name = f"500T-{attack_type.replace(' ', '-').lower()}-{metric_column.lower().split(' (')[0].replace(' ', '-')}"
        f.save_dataframe_as_csv(
            f"{c.REPORTED_DATA_DIRECTORY_PATH}/{reported_file_name}.csv", idle_attack_df
        )
        f.save_file(
            f"{c.TABLES_OUTPUT_DIRECTORY_PATH}/{reported_file_name}.tex", latex_table
        )
