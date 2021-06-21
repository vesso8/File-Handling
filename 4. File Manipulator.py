import os
def create_file(file_path):
    with open(file_path, "w") as file:
        file.write("")

def add_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content + "\n")

def replace_file(file_path,content, new_string):
    try:
        with open(file_path, "r+") as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(content, new_string)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print("An error occurred")

def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


actioner = {
    "Create": create_file,
    "Add": add_file,
    "Replace": replace_file,
    "Delete": delete_file,
}

def file_manipulator():
    command_data = input().split("-")
    while not command_data[0] == "End":
        command, command_args = command_data[0], command_data[1:]
        actioner[command](*command_args)
        command_data = input().split("-")

file_manipulator()