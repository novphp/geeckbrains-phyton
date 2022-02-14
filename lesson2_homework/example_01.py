# Урок 2 / Задание 1 (on check)

multitype_list = [1, 84612, 45.3, 'string', False, None, range(6), (1, 2, 3), [1, 2], {1: 'res1'}]

i = 1
for item in multitype_list:
    print(f"Элемент {i} - {item}, тип - {type(item)}")
    i += 1
