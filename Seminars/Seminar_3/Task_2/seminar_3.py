# 4. Задайте список из 2*N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

try:
    list = []
    N = int(input("Введите число "))

    for i in range(-N, N+1):
        list.append(i)
    with open('file.txt', 'r') as data:
        a = data.readline()
        b = data.readline()

    print(a, b)
    a = int(a)
    b = int(b)
    print(list)
    print(f'Произведение элементов равно {list[a]*list[b]}')


except:
    print("надо было вводить именно целое число")
