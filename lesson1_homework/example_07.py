# Урок 1 / Задание 7

res_start = int(input("Результат пробежки в первый день (км): "))
res_desired = int(input("Какой результат необходимо достигнуть (км): "))
day_counter = 1
day_ratio = 0.1 # Коэфициент ежедневного улучшения результата

while res_start < res_desired:
    res_start += res_start * day_ratio
    day_counter += 1

if day_counter % 10 == 1 and day_counter != 11:
    ending = 'день'
elif 1 < day_counter % 10 < 5 and (day_counter < 5 or day_counter > 14):
    ending = 'дня'
else:
    ending = 'дней'

print(f"Желаемый результат будет достигнут за {day_counter} {ending}")
