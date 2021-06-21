import os

def extract_files(dir):
    return [el for el in dir if "." in el]

def file_extensions(files):
    report = {}
    for file in files:
        file_name , extensions = file.split(".")
        if extensions not in report:
            report[extensions] = []
        report[extensions].append(file_name)
    return report

dir_content = os.listdir()

files = extract_files(dir_content)
report_info = file_extensions(files)

for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    print(f".{extension}")
    print(*[f"- - - {name}.{extension}" for name in file_names], sep= '\n')