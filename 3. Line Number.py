import re
letter_path = r"[a-zA-Z]"
punctuation_path = r"[-/,/./!/?/']"

def symbs(line, path):
    return len(re.findall(path,line))
with open("line.txt") as file:
    counter = 1
    lines_nums = file.readlines()
    for lines in lines_nums:
        letter = symbs(lines, letter_path)
        punctuation_marks = symbs(lines, punctuation_path)
        print(f"Line {counter}: {lines[:-1]}({letter})({punctuation_marks})")
        counter += 1
