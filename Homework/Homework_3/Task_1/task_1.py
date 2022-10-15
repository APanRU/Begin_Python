# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers_list = [2, 3, 5, 9, 3]


def odd_numbers_summ(x):
    summ = 0
    for i in range(len(x)):
        if i % 2 != 0:
            summ += x[i]
    return summ


print(odd_numbers_summ(numbers_list))
