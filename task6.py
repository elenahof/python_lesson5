import re

subj = {}
with open('task_6.txt', 'r') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        subj.update({row_items[0]: sum([int(i) for i in hours])})

print("Total number of lessons: ", subj)