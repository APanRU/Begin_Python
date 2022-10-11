# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     *Пример:*
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Enter X coordinate of point 1: "))
y1 = float(input("Enter Y coordinate: of point 1: "))

x2 = float(input("Enter X coordinate of point 2: "))
y2 = float(input("Enter Y coordinate: of point 2: "))

result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(round(result, 3))
