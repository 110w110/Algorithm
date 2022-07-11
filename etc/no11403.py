import sys

N = int(sys.stdin.readline())
P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for m in range(N):
    for i in range(N):
        for j in range(N):
            if P[i][m]==1 and P[m][j]==1:
                P[i][j]=1

for _ in range(N):
    print(*P[_])