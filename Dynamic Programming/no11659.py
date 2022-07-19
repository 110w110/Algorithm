import sys
N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
P = [(tuple(map(int, sys.stdin.readline().split()))) for _ in range(M)]

points = list(set(sum(P,())))

R = [0 for _ in range(len(L)+1)]

for i in range(1,len(R)):
    R[i] += R[i-1] + L[i-1]

for s,t in P:
    print(R[t]-R[s-1])