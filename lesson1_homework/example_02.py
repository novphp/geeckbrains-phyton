# Урок 1 / Задание 2

sec_in_hour = 60 * 60
max_sec = 99 * sec_in_hour + 59 * 60 + 59
user_time = int(input("Введите количество секунд: "))
if user_time <= max_sec:
    time_s = user_time % 60
    time_m = user_time // 60 - user_time // sec_in_hour * 60
    time_h = user_time // sec_in_hour
    print(f"{time_h:02}:{time_m:02}:{time_s:02}")
else:
    print(f"Ошибка, превышено максимальное значение {max_sec}")
