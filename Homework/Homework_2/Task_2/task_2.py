# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(a):
    numbers = []
    value = 1
    for i in range(1, N+1):
        numbers.append(value)
        value *= i+1
    return numbers


try:
    N = int(input("Введите число: "))
    print(factorial(N))

except:
    print("Введены некорректные данные!")
