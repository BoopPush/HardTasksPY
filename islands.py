xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]

a = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 1]
]

n, m = 3, 3
stack = []
k = 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            k += 1
            a[i][j] = k
            stack.append(i)
            stack.append(j)
            while len(stack):
                y = stack.pop()
                x = stack.pop()
                for l in range(4):
                    if 0 <= x + xx[l] < n and 0 <= y + yy[l] < m:
                        if a[x + xx[l]][y + yy[l]] == 1:
                            a[x + xx[l]][y + yy[l]] = k
                            stack.append(x + xx[l])
                            stack.append(y + yy[l])

print(k - 1)
for i in range(n):
    print(a[i])
