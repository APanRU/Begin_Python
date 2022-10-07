# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

from tokenize import Double


n = float(input("Enter number N\n"))
if m == (n * 10) % 10:
    print(int(m))
else:
    print("нет")


