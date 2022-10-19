# Задача 1

# def f(x):
#     return x**2


# g = f
# print(type(f))
# print(type(g))
# print(g(4))
# print(f(4))

# Задача 2

# def calc1(x):
#     return x + 10


# print(calc1(10))


# def calc2(x):
#     return x * 10


# print(calc2(10))
# print(calc1(10))


# def math(op, x):
#     print(op(x))


# math(calc2, 10)

# Задача 3

# from pickletools import read_uint1
# import re


# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y

# def mylt(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)


# calc(lambda x, y: x+y, 4, 5)

# Задача 4

# list = []

# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append(i)
# print(list)

# list = []

# for i in range(1, 101):
#     # if (i % 2 == 0):
#     list.append(i)
# print(list)

# list = [i for i in range(1, 21)]
# print(list)


# list = [i for i in range(1, 21) if (i % 2 == 0)]
# print(list)


# list = [(i, i) for i in range(1, 21) if (i % 2 == 0)]
# print(list)

# def f(x):
#     return x**3


# list = [f(i) for i in range(1, 21) if (i % 2 == 0)]
# print(list)

# list = [(i, f(i)) for i in range(1, 21) if (i % 2 == 0)]
# print(list)

# Задача 5. В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить [(2,4), (8,64),(38,1444)]


# f = open(r"D:\geekbrains\Begin_Python\Lecture\Lecture_3\1.txt", 'r')
# data = f.read() + ' '
# print(data)
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# Функция map

# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, "1 2 3".split())

# for e in data:
#     print(e)

# print("___")

# for e in data:
#     print(e)

# data = list(map(int, "1 2 3".split()))

# for e in data:
#     print(e)

# print("___")

# for e in data:
#     print(e)


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция фильтр

# data = [x for x in range(10)]
# result = list(filter(lambda x: not x % 2, data))
# print(result)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция zip

user = ["user1", "user2", "user3", "user4", "user5"]
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

# data = list(zip(user, ids, salary))
# print(data)

data = list(enumerate(user))
print(data)
