import sys

n,m = map(int,sys.stdin.readline().split())
M = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
P = [[10**9 for _ in range(n)] for _ in range(n)]

# init
for s,t in M:
    P[s-1][t-1] = 1
    P[t-1][s-1] = 1

#Floyd
for m in range(n):
    for s in range(n):
        for t in range(n):
            if s==t:
                P[s][t] = 0
            if P[s][m] + P[m][t] <= P[s][t]:
                P[s][t] = P[s][m] + P[m][t]

for i in range(n):
    for j in range(n):
        if P[i][j]==int(10**9):
            P[i][j]=0

min = 10**9
mi = 0
for i in range(n):
    s = 0
    for j in range(n):
        s += P[i][j]
    if s<min:
        min = s
        mi = i

print(mi+1)