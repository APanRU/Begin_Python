# Задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
try:
    numbers_list = list(map(int, input("Введите числа через пробел:\n").split()))
    print(f"Исходный список: {numbers_list}")
    new_list = []
    [new_list.append(i) for i in new_list if i not in numbers_list]
    print(f"Список из неповторяющихся элементов: {new_list}")
except:
    print("Введены некорректные данные!")
