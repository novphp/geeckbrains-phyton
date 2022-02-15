# Урок 4 / Задание 2

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

output_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i-1] < source_list[i]]

print(f"Исходный список: {source_list}\nРезультат: {output_list}")
