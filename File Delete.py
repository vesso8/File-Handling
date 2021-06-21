import os
try:
    os.remove("some_tasks/text.txt")
except FileNotFoundError:
    print('File already deleted!')