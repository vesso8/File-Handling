import re
searched_words = []

with open("words.txt") as file:
    searched_words = file.read().lower().split()
count_collector = {}
with open("some_tasks/text.txt") as file:
    content = file.read().lower()
    for words in searched_words:
        result = re.findall(rf"(?<=(\-|\s)){words}(?=(\.|))", content)
        count_collector[words] = len(result)

sorted_result = sorted(count_collector.items(), key=lambda x: -x[1])
for key, value in sorted_result:
    print(f"{key} - {value}")