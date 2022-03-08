# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('tsk3.txt', 'r') as my_file:
    emp_list = []
    mid_sal = []
    my_list = my_file.read().split('\n')
    for line in my_list:
        line = line.split()
        if float(line[1]) < 20000:
            emp_list.append(line[0])
        mid_sal.append(line[1])
print('Список сотрудников, оклад которых менее 20 тыс.:', emp_list)
print('Средняя величина дохода сотруднико:', sum(map(float, mid_sal)) / len(mid_sal))