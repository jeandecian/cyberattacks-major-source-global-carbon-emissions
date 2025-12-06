import constants as c
import data_utils as d
import file_utils as f


for path in f.get_all_files_recursively(c.RAW_DATA_DIRECTORY_PATH):
    file_extension = f.get_file_extension(path)

    if file_extension not in (c.EXTENSION_CSV, c.EXTENSION_HTML, c.EXTENSION_LOG):
        continue

    if file_extension == c.EXTENSION_CSV:
        df = f.get_dataframe_from_csv(path)
    elif file_extension == c.EXTENSION_HTML:
        df = d.get_dataframe_from_html(path)
    elif file_extension == c.EXTENSION_LOG:
        df = f.get_dataframe_from_log(path)

    df = d.clean_dataframe(path, df)
    df = d.feature_dataframe(path, df)
    df = d.label_dataframe(path, df)
    df = d.reorder_dataframe_headers(df)

    path = path.replace(c.RAW, c.PREPROCESSED).replace(file_extension, c.EXTENSION_CSV)
    f.save_dataframe_as_csv(path, df)
