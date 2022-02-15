# Урок 4 / Задание 1

from sys import argv

def calc_salary():
    try:
        script_name, worktime, rate, bonus = argv
        zp = float(worktime) * float(rate) + float(bonus)
        print(f"Заработная плата: {zp}")
    except ValueError:
        print("Ошибка значения")

calc_salary()