import sys
from collections import deque

R, C, T = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
direction = [(0,-1),(0,1),(-1,0),(1,0)]
#상하좌우
for time in range(T):
    #확산
    # 미세먼지 있는 칸 큐에 삽입
    # 하니씩 pop해 인접한 4방향에 확산
    Q = deque()
    for r in range(R):
        for c in range(C):
            if A[r][c]!=0 and A[r][c]!=-1:
                Q.append((r,c))
    B = [[0 for _ in range(C)] for _ in range(R)]
    for r,c in Q:
        dust = A[r][c]
        D = deque()
        if r>0:             #상 가능
            if A[r-1][c]!=-1:
                D.append(direction[0])
        if r<R-1:           #하 가능
            if A[r+1][c] != -1:
                D.append(direction[1])
        if c>0:             #좌 가능
            if A[r][c-1]!=-1:
                D.append(direction[2])
        if c<C-1:           #우 가능
            if A[r][c+1]!=-1:
                D.append(direction[3])

        dp = dust//5
        A[r][c] = dust - len(D)*dp
        for x,y in D:
            B[r+y][c+x] += dp

    for r in range(R):
        for c in range(C):
            B[r][c] += A[r][c]

    #순환
    A = [c[:] for c in B]
    ac = 0
    while True:
        if A[ac][0]==-1:
            break
        ac += 1
    #우 좌
    for x in range(1,C-1):
        A[ac][x+1] = B[ac][x]
        A[ac+1][x+1] = B[ac+1][x]
    for x in range(C-1,0,-1):
        A[0][x-1] = B[0][x]
        A[R-1][x-1] = B[R-1][x]
    A[ac][1]=0
    A[ac+1][1]=0
    #상 하
    for y in range(ac,-1,-1):
        A[y-1][C-1] = B[y][C-1]
    for y in range(R-1,ac+2,-1):
        A[y-1][0] = B[y][0]
    for y in range(ac+1,R-1):
        A[y+1][C-1] = B[y][C-1]
    for y in range(0,ac-1):
        A[y+1][0] = B[y][0]

result = 0
for r in range(R):
    for c in range(C):
        result += A[r][c]
print(result+2)