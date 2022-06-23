import sys
from collections import deque

X, Y = map(int,sys.stdin.readline().split())
T = [list(map(int,sys.stdin.readline().split())) for _ in range(Y)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
count = 0

global new
new = deque()
q = deque()

def ripe(x,y):
    c = False
    for d in direction:
        dx = x + d[0]
        dy = y + d[1]
        if dx < X and dx >=0 and dy < Y and dy >=0:
            if T[dy][dx]==0:
                T[dy][dx]=1
                new.append((dx,dy))
                c = True
    return c

def search():
    unripen = 0
    for i in range(Y):
        for j in range(X):
            if T[i][j]==1:
                q.append((j,i))
            elif T[i][j]==0:
                unripen += 1
    return unripen

u = search()
while True:
    isChanged = False
    while q:
        x, y = q.popleft()
        if ripe(x,y) == True:
            isChanged = True
    q.extend(new)
    new.clear()
    if isChanged == False:
        if search() != 0:
            count = -1
        break
    count += 1
print(count)