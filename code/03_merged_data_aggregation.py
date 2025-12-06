import constants as c
import file_utils as f

df = f.get_dataframe_from_csv(f"{c.PROCESSED_DATA_DIRECTORY_PATH}/merged/merged.csv")
df = df.drop(columns=[c.MEASUREMENT, c.TIMESTAMP, c.TIMESTAMP_RELATIVE])

grouping_columns = [c.ATTACK_TYPE, c.ATTACK, c.HOST, c.RUN, c.MODE]
metric_columns = [col for col in df.columns if col not in grouping_columns]

df_means = df.groupby(grouping_columns)[metric_columns].mean().round(2).reset_index()

f.save_dataframe_as_csv(
    f"{c.PROCESSED_DATA_DIRECTORY_PATH}/aggregated/means.csv", df_means
)
