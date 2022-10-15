# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def summ_number(a):
    a = int(str(a).replace(".", ""))
    result = 0
    while a != 0:
        result += a % 10
        a //= 10
    return result


try:
    a = float(input("Введите число: "))
    print("Сумма цифр числа = ", summ_number(a))

except:
    print("Введены некорректные данные!")

# number = input("Введите число: ")
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(sum)
