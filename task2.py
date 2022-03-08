# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
try:
    my_file = open('task_2.txt')

    x = 0
    for line in my_file.readlines():
        x += 1
    print("Количество строк в файле: ", x)
    my_file.close()
    my_file = open('task_2.txt')
    a = 0
    for line_2 in my_file.readlines():
        print(f'Количество слов в строке {a + 1}: {len(line_2.split())}')
except FileNotFoundError:
    print('File not found!')
finally:
    my_file.close()
