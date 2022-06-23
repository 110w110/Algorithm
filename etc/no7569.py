import sys
from collections import deque

X, Y, Z = map(int,sys.stdin.readline().split())
T = [[list(map(int,sys.stdin.readline().split())) for _ in range(Y)] for _ in range(Z)]
direction = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
count = 0

global new
new = deque()
q = deque()

def ripe(x,y,z):
    c = False
    for d in direction:
        dx = x + d[0]
        dy = y + d[1]
        dz = z + d[2]
        if dx < X and dx >=0 and dy < Y and dy >=0 and dz < Z and dz >=0:
            if T[dz][dy][dx]==0:
                T[dz][dy][dx]=1
                new.append((dx,dy,dz))
                c = True
    return c

def search():
    unripen = 0
    for k in range(Z):
        for i in range(Y):
            for j in range(X):
                if T[k][i][j]==1:
                    q.append((j,i,k))
                elif T[k][i][j]==0:
                    unripen += 1
    return unripen

u = search()
while True:
    isChanged = False
    while q:
        x, y, z = q.popleft()
        if ripe(x,y,z) == True:
            isChanged = True
    q.extend(new)
    new.clear()
    if isChanged == False:
        if search() != 0:
            count = -1
        break
    count += 1
print(count)