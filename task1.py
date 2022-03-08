# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('task_1.txt', 'w')
inp = input("Введите текст для записи в файл: \n")
while inp:
    my_file.writelines(inp)
    inp = input("Введите текст для записи в файл: \n")
    if not inp:
        break
my_file.close()

my_file = open('task_1.txt', 'r')
readit = my_file.readlines()
print(readit)
my_file.close()
