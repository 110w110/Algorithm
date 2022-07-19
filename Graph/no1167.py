import sys

n = int(sys.stdin.readline())

M = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
P = [[10001 for _ in range(n)] for _ in range(n)]

for m in M:
    a = m[0]
    while len(m)>2:
        P[a-1][m[-3]-1] = m[-2]
        del m[-3:-1]

# print(*P,sep='\n')

# # init
# for s,t,cost in M:
#     if P[s-1][t-1] > cost:
#         P[s-1][t-1] = cost

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
        if P[i][j]==int(10001):
            P[i][j]=0

# for _ in range(n):
#     print(*P[_])
max=0
for i in range(n):
    for j in range(n):
        if P[i][j]>max:
            max = P[i][j]

print(max)