# Генератор размещений
from itertools import *

m = input("Enter word: ")
n = int(input(":"))

for i in product(m, repeat=n):
    print(i, end=' ')
