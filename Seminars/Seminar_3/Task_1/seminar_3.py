# 3. Задайте список из n чисел последовательности (1+1/N)**N  и выведите на экран их сумму.

# n = int(input('Enter number: '))


# def sequence(n):
#     return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]


# print(sequence(n))
# print(round(sum(sequence(n))))

# Вариант решения №2

# def posl(a):
#     return (1+1/a)**a


# n = int(input('Введите число: '))
# sp = []
# for i in range(n):
#     sp.append(posl(i + 1))
# print(sum(sp))
