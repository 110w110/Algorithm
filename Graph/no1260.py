import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())

G = [[0 for _ in range(N)] for _ in range(N)]
I = [tuple(map(int,sys.stdin.readline().split())) for _ in range(M)]

for a,b in I:
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1

bfs_visited = [False for _ in range(N)]
bfs_q = deque()
bfs_r = deque()
dfs_visited = [False for _ in range(N)]
dfs_q = deque()
dfs_r = deque()

def dfs(node):
    dfs_r.append(node)
    dfs_visited[node-1] = True
    for i in range(N):
        x = G[node-1][i]
        if x==1 and dfs_visited[i]==False:
            dfs(i+1)
dfs(V)
bfs_q.append(V)
while bfs_q:
    node = bfs_q.popleft()
    bfs_r.append(node)
    bfs_visited[node-1] = True
    for i in range(N):
        x = G[node-1][i]
        if x==1:
            if bfs_visited[i]==False:
                bfs_q.append(i+1)
                bfs_visited[i]=True

print(*dfs_r)
print(*bfs_r)
