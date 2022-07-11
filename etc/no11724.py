import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().split())
E = [tuple(map(int,sys.stdin.readline().split())) for _ in range(M)]

result = 0

P = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]

for u,v in E:
    P[u-1][v-1]=1
    P[v-1][u-1]=1

def dfs(n):
    visited[n]=1
    for j in range(N):
        if P[n][j] and visited[j]==0:
            dfs(j)

for i in range(N):
    if visited[i]!=0:
        continue
    dfs(i)
    result += 1

# print(*P,sep='\n')
# print(*visited)

print(result)