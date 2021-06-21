# try:
#     text = open("text.txt")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")


from os import path

if path.exists("some_tasks/text.txt"):
    print("File found")
else:
    print("File not found")