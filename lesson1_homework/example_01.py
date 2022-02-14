# Урок 1 / Задание 1

current_date = "31.01.2020"
current_price = 1000
# скидка за каждую дополнительную единицу товара
count_rate = 0.05
products_name = input("Введите наименование товара: ")
products_count = int(input("Введите необходимое количество (1-10): "))
if products_count <= 10:
    summ = current_price * products_count * (1 - (count_rate * (products_count - 1)))
    print(f"На {current_date} стоимость \"{products_name}\", в количестве {products_count} составит: {summ} Руб.")
    print(type(summ))
else:
    print("Некорректное количество")
