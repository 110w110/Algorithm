import sys

def robot(R,C,D):
    count = 0
    direction = [(0,-1),(1,0),(0,1),(-1,0)]
    d = D
    r = R
    c = C
    if A[R][C]!=0:
        return
    while True:
        count += 1
        A[r][c] = -1
        times = 0
        while True:
            d = (d-1)%4
            dx = c + direction[d][0]
            dy = r + direction[d][1]
            if times>=4:
                d = (d+1)%4
                if A[r-direction[d][1]][c-direction[d][0]]!=1:
                    c = c-direction[d][0]
                    r = r-direction[d][1]
                    break
                else:
                    return
            if A[dy][dx]!=0:
                times += 1
                continue
            else:
                c = dx
                r = dy
                break

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

prev = 0
next = 0
for i in range(N):
    for j in range(M):
        if A[i][j]==0:
            prev +=1
robot(r,c,d)
for i in range(N):
    for j in range(M):
        if A[i][j]==0:
            next +=1
print(prev-next)