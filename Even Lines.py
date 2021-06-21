import re
def replace_symbols(line):
    return re.sub(r"[-/,/./!/?]" , "@", line)

with open("even_lines_text.txt") as file:
    even_lines_sentence = file.readlines()
    for row_number in range(len(even_lines_sentence)):
        if row_number % 2 == 0:
            replaced = replace_symbols(even_lines_sentence[row_number]).split()
            print(' '.join(replaced[::-1]))