"""
4) Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
"""

user_num = int(input("Введите целое положительное число: "))
max_digit = 0
while user_num != 0:
    digit = user_num % 10
    if digit > max_digit:
        max_digit = digit
    user_num //= 10

print(f"Самая большая цифра в числе: {max_digit}")
