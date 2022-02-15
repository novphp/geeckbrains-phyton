# Урок 4 / Задание 5

from functools import reduce

def calc( el1, el2):
    return  el1 * el2

#source_list = [item for item in range(10, 13)]
source_list = [item for item in range(100, 1001, 2)]
res = reduce(calc, source_list)

print(f"Произведение всех элементов списка: {res}")
