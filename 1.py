# Генератор сочетаний(без повторений) C(m,n)

from itertools import *

m = input("Enter word: ")
n = int(input(":"))
for i in combinations(m, n):
    print(i, end=' ')

print("""
----------
        """)
# Генератор сочетаний(с повторениями) C(m,n)
for i in combinations_with_replacement(m,n):
    print(i,end=' ')
