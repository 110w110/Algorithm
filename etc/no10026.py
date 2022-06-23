import sys
from collections import deque

N = int(sys.stdin.readline())
I = [sys.stdin.readline() for _ in range(N)]
V = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()
q2 = deque()

def near(x,y,k,c):
    if k==True:
        color= {'R':'R','G':'R','B':'B'}
        v=1
    else:
        color= {'R':'R','G':'G','B':'B'}
        v=0
    cur = color.get(c)
    V[v][y][x]=1

    for d in direction:
        dx = x + d[0]
        dy = y + d[1]
        if dx >= 0 and dx < N and dy >= 0 and dy < N:
            if V[v][dy][dx]!=1:
                if color.get(I[dy][dx]) in cur:
                    if k==True:
                        if (dx,dy) not in q2:
                            q2.append((dx,dy))
                    else:
                        if (dx,dy) not in q:
                            q.append((dx,dy))

count = [0,0]
for i in range(N):
    for j in range(N):
        area = [0,0]
        if V[0][i][j]!=1:
            c = I[i][j]
            near(j,i,False,c)
            if len(q)==0:
                area[0] = 1
            while q:
                qi = q.popleft()
                area[0] += 1
                near(qi[0],qi[1],False,c)
        if V[1][i][j]!=1:
            near(j,i,True,c)
            if len(q2)==0:
                area[1] = 1
            while q2:
                qi = q2.popleft()
                area[1] += 1
                near(qi[0],qi[1],True,c)
        if area[0]!=0:
            count[0] += 1
        if area[1]!=0:
            count[1] += 1

print(*count)