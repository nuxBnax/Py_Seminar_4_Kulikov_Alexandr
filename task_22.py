# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих 
# наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества. Затем
# пользователь вводит сами элементы множеств.

from random import randint

n = int(input('Enter size of list_n: '))
m = int(input('Enter size of list_m: '))

list_n = [randint(-10, 10) for i in range(n)]
list_m = [randint(-10, 10) for i in range(m)]
print(list_n)
print(list_m)

list_n = set(list_n)
list_m = set(list_m)
print(list_n)
print(list_m)

list_1 = list_n.intersection(list_m)

list_2 = list(list_1)
print(list_2)

for i in range(len(list_2) - 1):
    for j in range(len(list_2) - i - 1):
        if list_2[j] > list_2[j + 1]:
            (list_2[j], list_2[j + 1]) = (list_2[j + 1], list_2[j]) 
print(list_2)


