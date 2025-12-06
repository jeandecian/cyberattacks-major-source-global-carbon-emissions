import constants as c
import data_utils as d
import file_utils as f

dfs = []

for file_path in f.get_all_files_recursively(c.PREPROCESSED_DATA_DIRECTORY_PATH):
    file_extension = f.get_file_extension(file_path)

    if file_extension != c.EXTENSION_CSV:
        continue

    dfs.append(f.get_dataframe_from_csv(file_path))

merged_df = d.concat_dataframes(dfs)
merged_df = d.reorder_dataframe_headers(merged_df)

f.save_dataframe_as_csv(
    f"{c.PROCESSED_DATA_DIRECTORY_PATH}/merged/merged.csv", merged_df
)
