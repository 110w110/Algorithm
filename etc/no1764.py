import sys

n, m = map(int,sys.stdin.readline().split())
N = []
M = []
for _ in range(n):
    N.append(sys.stdin.readline().strip())
for _ in range(m):
    M.append(sys.stdin.readline().strip())

N.sort()
M.sort()

R = []

i = 0
for x in N:
    while True:
        if i >= len(M):
            break
        elif M[i]==x:
            R.append(x)
            break
        elif M[i]<x:
            i += 1
        else:
            break

print(len(R))
for y in R:
    print(y)