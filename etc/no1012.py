import sys
sys.setrecursionlimit(100000000)
T = int(sys.stdin.readline())
data = []
direction = [(0,-1),(0,1),(-1,0),(1,0)]

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    tmp = [tuple(map(int,sys.stdin.readline().split())) for _ in range(K)]
    data.append((_,M,N,K,tmp))

def check(x,y,m,n):
    result = []
    if x>0:
        result.append((x-1,y))
    if x<m-1:
        result.append((x+1,y))
    if y>0:
        result.append((x,y-1))
    if y<n-1:
        result.append((x,y+1))
    return result

for t, m, n, k, d in data:
    A = [[0 for _ in range(m)] for _ in range(n)]
    for X, Y in d:
        A[Y][X] = 1

    def dfs(x,y,m,n):
        for cx, cy in check(x, y, m, n):
            if A[cy][cx] == 1:
                A[cy][cx] = 2
                dfs(cx,cy,m,n)
            elif A[cy][cx] == 0:
                A[cy][cx] = -1

    count = 0
    for y in range(n):
        for x in range(m):
            if A[y][x]==-1 or A[y][x]==2:
                continue
            elif A[y][x]==1:
                A[y][x]=2
            elif A[y][x]==0:
                A[y][x]=-1
                continue
            dfs(x,y,m,n)
            count += 1

    print(count)
