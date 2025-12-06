import constants as c
import file_utils as f


markdown = "# Raw Data Inventory\n\n"
markdown += "## Inventory\n\n"
markdown += "| File | Cyberattack Type | Cyberattack Identifier | Host Identifier | Measurement Identifier | Run Identifier | Extension |\n"
markdown += "| --- | --- | --- | --- | --- | --- | --- |\n"

for file_path in f.get_all_files_recursively(c.RAW_DATA_DIRECTORY_PATH):
    file_name = f.get_file_name(file_path)
    file_elements = f.get_file_name_elements(file_name)

    if file_elements is None:
        continue

    run_identifier = "" if len(file_elements) == 5 else file_elements[4]

    markdown += f"| {file_name} | {' | '.join(file_elements[:4])} | {run_identifier} | {file_elements[-1]} |\n"

f.save_file(f"{c.RAW_DATA_DIRECTORY_PATH}/README.md", markdown)
