"""
2) Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
seconds = int(input("Введите время в секундах: "))

minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60

if hours > 99:
    print("Вы ввели слишком большое число")
else:
    seconds_1 = seconds % 10
    seconds_10 = seconds // 10
    minutes_1 = minutes % 10
    minutes_10 = minutes // 10
    hours_1 = hours % 10
    hours_10 = hours // 10

    print(
        f"Время в формате чч:мм:сс - {hours_10}{hours_1}:{minutes_10}"
        f"{minutes_1}:{seconds_10}{seconds_1}")
