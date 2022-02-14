# Урок 2 / Задание 5 (on check)

my_list = [8, 7, 5, 5, 4, 2, 1]
print(f"Исходный рейтинг: {my_list}")

while True:
    user_number = input("Введите новый элемент рейтинга (натуральное число), для завершения введите 'q': ")
    if user_number.upper() == "Q":
        print("Работа завершена")
        break
    i = 0
    for el in my_list:
        if int(user_number) <= el:
            i += 1
        else:
            my_list.insert(i, int(user_number))
            break
    print(f"Новый рейтинг: {my_list}")
