import constants as c
import file_utils as f


markdown = "# Raw Data Inventory\n\n"
markdown += "## Inventory\n\n"
markdown += "| File | Cyberattack Type | Cyberattack Identifier | Host Identifier | Measurement Identifier | Run Identifier | Extension |\n"
markdown += "| --- | --- | --- | --- | --- | --- | --- |\n"

for file_path in f.get_all_files_recursively(c.RAW_DATA_DIRECTORY_PATH):
    file_path = file_path.split("/")[-1]
    file_elements = file_path.split("_")
    nb_elements = len(file_elements)

    if nb_elements < 4:
        continue

    cyberattack_type = file_elements[0]
    cyberattack_identifier = file_elements[1]
    host_identifier = file_elements[2]

    if nb_elements == 4:
        measurement_identifier, extension = file_elements[3].split(".")
        run_identifier = ""
    elif nb_elements == 5:
        measurement_identifier = file_elements[3]
        run_identifier, extension = file_elements[4].split(".")

    markdown += f"| {file_path} | {cyberattack_type} | {cyberattack_identifier} | {host_identifier} | {measurement_identifier} | {run_identifier} | {extension} |\n"

f.save_file(f"{c.RAW_DATA_DIRECTORY_PATH}/README.md", markdown)
