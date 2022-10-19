# Задача 5. Задайте число. Составьте список чисел Фибонначи, в том числе для отрицательных индесов.
# Пример: - для к = 8 список будет выглядеть так: [-21,13,-8,5,-3,2-,1,0,1,1,2,3,8,13,21]


# fibanachchi = []
# n = int(input("Введите размер списка: "))

# for i in range(n):
#     if i == 0:
#         fibanachchi.append(0)
#     elif i == 1:
#         fibanachchi.append(1)
#     else:
#         fibanachchi.append(fibanachchi[i-1]+i)

# print(fibanachchi)


def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def Negafibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


list = [0]
user_number = int(input("Введите размер списка: "))
for i in range(1, user_number + 1):
    list.append(Fibonacci(i))
    list.insert(0, Negafibonacci(i))
print(list)
