import os


def get_all_files_recursively(path):
    files = []

    for root, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    return sorted(files)


def save_file(path, content):
    with open(path, "w") as f:
        f.write(content)
