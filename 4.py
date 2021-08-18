# Итератор , который возвращает размещения
from itertools import *

m = input(": ")
n = int(input(": "))

for i in permutations(m, n):
    print(i, end=' ')
