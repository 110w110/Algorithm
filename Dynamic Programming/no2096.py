import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
R = [P[i] for i in range(3)]

for _ in range(1,N):
    I = tuple(map(int,sys.stdin.readline().split()))
    T = [0 for _ in range(3)]
    T[0] = max(P[0]+I[0],P[1]+I[0])
    T[1] = max(P[0]+I[1],P[1]+I[1],P[2]+I[1])
    T[2] = max(P[1]+I[2],P[2]+I[2])
    P[0],P[1],P[2] = T[0],T[1],T[2]

    T[0] = min(R[0]+I[0],R[1]+I[0])
    T[1] = min(R[0]+I[1],R[1]+I[1],R[2]+I[1])
    T[2] = min(R[1]+I[2],R[2]+I[2])
    R[0],R[1],R[2] = T[0],T[1],T[2]

print(max(P),min(R))