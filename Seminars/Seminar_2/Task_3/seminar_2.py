# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81


try:
    n = int(input('Введите N: '))
    for i in range(0, n):
        print(((-3)**i), end=" ")
except:
    print('Неправильно введено число!')
