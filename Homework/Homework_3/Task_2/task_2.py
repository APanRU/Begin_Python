# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication_list(lst):
    if len(lst) % 2 != 0:
        x = len(lst)//2 + 1
    else:
        x = len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(x)]
    return new_lst


test_list = [2, 3, 4, 5, 6]
print(multiplication_list(test_list))

try:
    random_list = list(map(int, input("Введите числа через пробел: ").split()))
    print(multiplication_list(random_list))
except:
    print("Введены некорректные данные!")
