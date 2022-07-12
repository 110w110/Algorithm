import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

M = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]

P = [[10**12 for _ in range(n)] for _ in range(n)]

# init
for s,t,cost in M:
    if P[s-1][t-1] > cost:
        P[s-1][t-1] = cost

#Floyd
for s in range(n):
    for t in range(n):
        for m in range(n):
            if s==t:
                continue
            if P[s-1][m-1] + P[m-1][t-1] <= P[s-1][t-1]:
                P[s-1][t-1] = P[s-1][m-1] + P[m-1][t-1]

for i in range(n):
    for j in range(n):
        if P[i][j]==10**12:
            P[i][j]=0

for _ in range(n):
    print(*P[_])

# print(*M,sep='\n')