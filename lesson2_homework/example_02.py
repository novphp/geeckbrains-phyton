# Урок 2 / Задание 2 (on check)

user_data = input("Введите числа для заполнения списка, разделив пробелом: ")
_list = user_data.split()
print(f"Исходный список: {_list}")

i = 0
while i < len(_list) - 1:
    tmp = _list[i]
    _list[i] = _list[i + 1]
    _list[i + 1] = tmp
    i += 2

print(f"Результат: {_list}")
