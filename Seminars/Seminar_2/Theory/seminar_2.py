# Словари

book={}

book['Миша'] = 98465566
book['Саша']=[64654464,46546464]

print(book)

if 'Даша' in book:
    print("Yes")
else: print("No")

for x,y in book.items():
    print(x, y)
    

for x in book.values():
    print(x)

for x in book.keys():
    print(x)

#  Списки

sp = []
sp.append(True)
sp = sp + [1213, "абба", 54654, [1,2,3,5] ]
print(sp)
sp.insert(1,999)
print("after insert ",sp)

print(sp[-1][-1])

a = sp.pop(-1)
print("after pop ", a)

a.remove(2)
print("after remove  ", a)
for i in a: print(i)

mas_2dim= [] 
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(i+j)
    mas_2dim.append(temp)

for i in range(len(mas_2dim)):
    print(mas_2dim[i])