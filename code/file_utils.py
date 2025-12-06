from bs4 import BeautifulSoup
import chardet
import constants as c
import os
import pandas as pd


def create_directory(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_all_files_recursively(path):
    files = []

    for root, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    return sorted(files)


def get_csv_separator(path, encoding=c.ENCODING_DEFAULT):
    with open(path, "r", encoding=encoding) as f:
        first_line = f.readline()

    return ";" if ";" in first_line else ","


def get_dataframe_from_csv(path):
    file_encoding = get_file_encoding(path)
    separator = get_csv_separator(path, file_encoding)

    return pd.read_csv(path, encoding=file_encoding, sep=separator)


def get_dataframe_from_log(path):
    data = read_file(path).strip().split("\n")

    return pd.DataFrame(data)


def get_file_encoding(path):
    with open(path, "rb") as f:
        result = chardet.detect(f.read())

    return result["encoding"]


def get_file_extension(path):
    return path.split(".")[-1]


def get_file_host(path):
    return path.split("_")[4]


def get_file_name(path):
    return path.split("/")[-1]


def get_file_name_elements(name):
    elements = name.split("_")

    if len(elements) < 4:
        return None

    return elements[: len(elements) - 1] + elements[-1].split(".")


def get_html_soup(path):
    with open(path, "r", encoding=c.ENCODING_DEFAULT) as f:
        return BeautifulSoup(f, "html.parser")


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def save_dataframe_as_csv(path, df):
    create_directory(path)
    df.to_csv(path, encoding=c.ENCODING_DEFAULT, index=False)


def save_file(path, content):
    with open(path, "w") as f:
        f.write(content)
