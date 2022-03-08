# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []

with open('task_4.txt', 'r') as my_file:
    #my_list = my_file.read().split('\n')
    for line in my_file:
        line = line.split(' ', 1)
        new_list.append(dict_rus[line[0]] + ' ' + line[1])
    print(new_list)

with open('task_4_new.txt', 'w') as file_new:
    file_new.writelines(new_list)