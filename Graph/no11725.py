import sys

N = int(sys.stdin.readline())
E = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N-1)]
P = [[0 for _ in range(N)] for _ in range(N)]

for a,b in E:
    P[a-1][b-1]=1
    P[b-1][a-1]=1

print(*P,sep='\n')