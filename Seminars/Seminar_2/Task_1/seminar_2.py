# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input("Enter number of quadrant from 1(ONE) to 4(FOUR): "))

if x == 1:
    print("Range Y: is from 0 to pos.infinit; range X is from 0 to pos.infinit")
elif x == 2:
    print("Range Y: is from 0 to pos.infinit; range X is from 0 to neg.infinit")
elif x == 3:
    print("Range Y: is from 0 to neg.infinit; range X is from 0 to neg.infinit")
elif x == 4:
    print("Range Y: is from 0 to neg.infinit; range X is from 0 to pos.infinit")
else:
    print("Value must be rom 1(ONE) to 4(FOUR)")


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     *Пример:*
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21
