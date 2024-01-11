x, y = [int(t) for t in input().split()]
matrix = [[0] * y for _ in range(x)]


i = 0
m = 0
l = 0

while i != x*y:
    for k in range(l, y):
        if matrix[l][k] == 0:
            i += 1
            matrix[l][k] = i
        if k == y-1 or matrix[l][k+1] != 0:
            m = k
            extra = l+1
            break
    for f in range(extra, x):
        if matrix[f][m] == 0:
            i += 1
            matrix[f][m] = i
        if f == x - 1 or matrix[f+1][m] != 0:
            l = f
            extra = m-1
            break
    for k in range(m-1, -1, -1):
        if matrix[l][k] == 0:
            i += 1
            matrix[l][k] = i
        if matrix[l][k-1] != 0:
            m = k
            extra = l-1
            break
    for f in range(l-1, -1, -1):
        if matrix[f][m] == 0:
            i += 1
            matrix[f][m] = i
        if f == x - 1 or matrix[f-1][m] != 0:
            l = f
            extra = m+1
            break

for i in matrix:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()

