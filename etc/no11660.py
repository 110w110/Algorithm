import sys

N, M = map(int,sys.stdin.readline().split())

P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
L = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

R = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        R[i+1][j+1] = R[i][j+1] + R[i+1][j] + P[i][j] - R[i][j]

def s(a,b,c,d):
    return R[d][c] - R[d][a-1] - R[b-1][c] + R[b-1][a-1]

for a,b,c,d in L:
    print(s(b,a,d,c))
