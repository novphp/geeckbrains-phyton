# Урок 1 / Задание 5-6

revenue = float(input("Введите сумму выручки организации: "))
costs = float(input("Введите сумму издержек организации: "))
profit = revenue - costs

if profit < 0:
    print(f"Сумма убытков организации составляет {-profit}")
elif profit > 0:
    print(f"Сумма прибыли органицации составляет {profit}")
    profitability = profit / revenue * 100
    print(f"Рентабельность составляет {profitability:.1f}%")
    personal_count = int(input("Введите количество сотрудников: "))
    personal_salary = profit / personal_count
    print(f"Зарплата каждого сотрудника составит {personal_salary:.2f}")
else:
    print(f"Органицация работает в 0")
