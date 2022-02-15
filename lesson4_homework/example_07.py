# Урок 4 / Задание 7

def fact(number):
    current = 1
    for i in range(1, number + 1):
        yield {'label': i, 'res': current }
        current *= i + 1

number = int(input("Введите число для вычисления факториала: "))
for el in fact(number):
    print(f"{el['label']}! = {el['res']}")
