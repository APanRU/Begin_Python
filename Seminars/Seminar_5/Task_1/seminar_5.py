# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x ^ 3 + 2*x ^ 2 + 6 и 7*x ^ 2+6*x+3, Тогда их сумма будет равна 5*x ^ 3 + 9*x ^ 2 + 6*x + 9

str1 = '5*x^3 + 2*x^2 + 6'
str2 = '7*x^2+6*x+3'


dict = {}


def x(strin):
    dict_f = {}
    for i in range(len(strin)-1):
        if strin[i] == 'x':
            if strin[i+1] == '^':
                tmp = int(strin[i+2])
                if strin[i-1] == '*':
                    koef = int(strin[i-2])
                    dict_f[tmp] = koef
                else:
                    koef = 1
                    dict_f[tmp] = koef

    return dict_f


dict = x(str1)
print(dict)
