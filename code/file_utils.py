import os


def get_all_files_recursively(path):
    files = []

    for root, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    return sorted(files)


def get_file_name(path):
    return path.split("/")[-1]


def get_file_name_elements(name):
    elements = name.split("_")

    if len(elements) < 4:
        return None

    return elements[: len(elements) - 1] + elements[-1].split(".")


def save_file(path, content):
    with open(path, "w") as f:
        f.write(content)
