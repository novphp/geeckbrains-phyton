# Урок 1 / Задание 4

num = num_tmp = int(input("Введите целое положительное число: "))
max_digit = 0

while num_tmp > 0:
    last_digit = num_tmp % 10
    if last_digit > max_digit:
        max_digit = last_digit
    num_tmp = num_tmp // 10

print(f"В числе {num} наибольшая цифра равна {max_digit}")
