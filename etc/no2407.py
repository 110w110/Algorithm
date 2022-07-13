import sys
n, m = map(int,sys.stdin.readline().split())

D, U = 1, 1
for d in range(m):
    D *= d+1
for u in range(n,n-m,-1):
    U *= u

print(U//D)