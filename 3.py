# Генератор перестановок
from itertools import *

n = input()
for i in permutations(n):
    print(i, end=' ')
