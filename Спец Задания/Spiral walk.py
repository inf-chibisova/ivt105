from random import random
N = 5
M = 6
a = []
n = 0
for i in range(N):
    z = []
    for j in range(M):
        n += 1
        z.append(n)
        print("%4d" % n, end='')
    print()
    a.append(z)
print()
 