# Урок 2 / Задание 4 (on check)

user_string = input("Введите строку из нескольких слов, разделённых пробелами: ")

for ind, el in enumerate(user_string.split()):
    print(f"{ind+1} - {el:.10}")
