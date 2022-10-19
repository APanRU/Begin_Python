from random import *

pred = [True, False]
kolvo = randint(5, 25)
predicates = [choice(pred)for _ in range(kolvo)]
print(predicates)
