import sys

C = int(sys.stdin.readline())
N = int(sys.stdin.readline())
L = []
for _ in range(N):
    L.append(tuple(map(int,sys.stdin.readline().split())))
A = [[0 for _ in range(C)] for _ in range(C)]

for a, b in L:
    A[a-1][b-1]=1
    A[b-1][a-1]=1
V = [-1 for _ in range(C)]
V[0] = 1
global count
count = -1

def dfs(n):
    l = A[n]
    global count
    count += 1
    for i in range(len(l)):
        if V[i]==-1 and l[i]==1:
            V[i]=1
            dfs(i)
dfs(0)
print(count)