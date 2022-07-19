import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
M = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
P = [[10**9 for _ in range(n)] for _ in range(n)]

# init
for s,t,cost in M:
    if P[s-1][t-1] > cost:
        P[s-1][t-1] = cost

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

for _ in range(n):
    print(*P[_])