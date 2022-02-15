# Урок 4 / Задание 4

source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [item for item in source_list if source_list.count(item) == 1]

print(f"Исходный список: {source_list}\nСписок уникальных значений: {new_list}")
