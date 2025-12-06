import constants as c
import file_utils as f
import numpy as np
import pandas as pd
import re


def clean_dataframe(file_path, df):
    file_name = f.get_file_name(file_path)

    missing_headers = c.DATA_FILES.get(file_name, {}).get("missing_headers", None)

    if missing_headers is not None:
        file_extension = f.get_file_extension(file_path)

        if file_extension == c.EXTENSION_CSV:
            df.loc[-1] = df.columns.tolist()
            df = df.sort_index().reset_index(drop=True)

        df.columns = missing_headers

    df.columns = [
        c.CLEANED_HEADERS.get(header, header) for header in df.columns.tolist()
    ]

    for header in df.columns:
        if header == c.TIMESTAMP:
            df[header] = (
                df[header]
                .str.split(" ")
                .str[-1]
                .str.split("–")
                .str[0]
                .str.replace("/", ":")
            )

            first_timestamp = df[header].iloc[0]
            last_timestamp = df[header].iloc[-1]

            timestamp_length = len(first_timestamp)

            if timestamp_length == 8:
                df[header] = df[header] + c.TIME_MILLI
            elif timestamp_length == 5:
                left_is_identical = first_timestamp[:2] == last_timestamp[:2]
                right_is_identical = first_timestamp[3:] == last_timestamp[3:]

                if left_is_identical and not right_is_identical:
                    df[header] = df[header] + c.TIME_ZERO_RIGHT + c.TIME_MILLI
                elif not left_is_identical and right_is_identical:
                    df[header] = c.TIME_ZERO_LEFT + df[header] + c.TIME_MILLI

            continue

        col_type = df[header].dtype

        if col_type == "object":
            for cleaned_data in c.CLEANED_DATA:
                df[header] = (
                    df[header]
                    .astype(str)
                    .str.replace(cleaned_data, c.CLEANED_DATA.get(cleaned_data, None))
                    .str.rstrip()
                )

            df[header] = pd.to_numeric(df[header], errors="coerce")

    return df


def feature_dataframe(file_path, df):
    if c.CPU_TEMPERATURE_MILLI in df.columns:
        df[c.CPU_TEMPERATURE] = df[c.CPU_TEMPERATURE_MILLI] / 1000

    if c.CURRENT_MILLI in df.columns:
        host = f.get_file_host(file_path)
        df[c.CURRENT] = df[c.CURRENT_MILLI] / 1000
        df[c.POWER] = df[c.CURRENT] * c.ACS712_VOLTAGES[host]

    if c.TIMESTAMP_RELATIVE in df.columns:
        td_series = df[c.TIMESTAMP_RELATIVE]

        H = (td_series // 3600).astype(int)
        M = ((td_series // 60) % 60).astype(int)
        S_f = td_series % 60

        df[c.TIMESTAMP] = [f"{h:02d}:{m:02d}:{s:06.3f}" for h, m, s in zip(H, M, S_f)]

    if c.CPU_USAGE_IDLE in df.columns:
        df[c.CPU_USAGE] = 100 - df[c.CPU_USAGE_IDLE]

    if c.MEMORY_USAGE_FREE_MO in df.columns and c.MEMORY_USAGE_TOTAL_MO in df.columns:
        df[c.MEMORY_USAGE] = (
            1 - df[c.MEMORY_USAGE_FREE_MO] / df[c.MEMORY_USAGE_TOTAL_MO]
        ) * 100

    return df


def get_dataframe_from_html(file_path):
    soup = f.get_html_soup(file_path)
    script = soup.find_all("script")[-1]
    script_text = script.get_text()

    pattern = re.compile(c.REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY, re.S)

    dfs = []

    for ressource, text in pattern.findall(script_text):
        if ressource in ("data_CPU_USE", "data_TOPDISK"):
            continue

        data = parse_google_visualization_array(text)

        df = pd.DataFrame(data[1:], columns=data[0])
        df = df.rename(
            columns={
                column: f"{ressource}_{column}"
                for column in df.columns
                if column != c.TIMESTAMP
            }
        )

        dfs.append(df)

    return merge_dataframes(dfs, c.TIMESTAMP, "outer")


def label_dataframe(file_path, df):
    file_name = f.get_file_name(file_path)
    configuration = c.DATA_FILES.get(file_name, {}).get("attack_configuration", None)
    configuration_type = type(configuration)

    df[c.MODE] = ""

    if configuration_type == dict:
        modes = len(configuration)

        for mode, timestamp in configuration.items():
            condition = timestamp <= df[c.TIMESTAMP]
            df[c.MODE] = np.where(condition, mode.capitalize(), df[c.MODE])
    elif configuration_type == int:
        mode_segment_size = configuration
        rows_count = df.shape[0]
        modes = round(rows_count / configuration)

        if modes == 2:
            condition = df.index < mode_segment_size
            df[c.MODE] = np.where(condition, c.ATTACK_MODES[0], c.ATTACK_MODES[1])
        elif modes == 3:
            conditions = [
                df.index < mode_segment_size,
                (df.index >= mode_segment_size) & (df.index < 2 * mode_segment_size),
                df.index >= 2 * mode_segment_size,
            ]
            df[c.MODE] = np.select(conditions, c.ATTACK_MODES, default="")

    file_name_elements = f.get_file_name_elements(file_name)
    df[c.ATTACK_TYPE] = c.ATTACK_TYPES.get(file_name_elements[0], file_name_elements[0])
    df[c.ATTACK] = c.ATTACK_NAMES.get(file_name_elements[1], file_name_elements[1])
    df[c.HOST] = c.HOST_NAMES.get(file_name_elements[2], file_name_elements[2])
    df[c.MEASUREMENT] = c.MEASUREMENT_TOOLS.get(
        file_name_elements[3], file_name_elements[3]
    )
    df[c.RUN] = int(file_name_elements[4]) if len(file_name_elements) == 6 else 1

    return df


def merge_dataframes(dfs, merge_on, merge_how):
    merged_df = dfs[0]

    for df in dfs[1:]:
        merged_df = merged_df.merge(df, on=merge_on, how=merge_how)

    return merged_df


def parse_google_visualization_array(data):
    header_pattern = re.compile(c.REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY_HEADER, re.S)
    row_pattern = re.compile(c.REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY_ROW, re.S)

    header = [c.TIMESTAMP] + [
        part.strip("'") for part in header_pattern.findall(data)[0].split(",")
    ]
    rows = []

    for datetime, values in row_pattern.findall(data):
        time = ":".join([part.strip() for part in datetime.split(",")[3:]])

        rows.append([time] + values.split(","))

    rows.insert(0, header)

    return rows


def reorder_dataframe_headers(df):
    return df[[header for header in c.ORDERED_HEADERS if header in df.columns]]
