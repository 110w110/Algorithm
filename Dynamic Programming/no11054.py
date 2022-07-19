import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
R = [1 for _ in range(N)]
S = [1 for _ in range(N)]

for i in range(1,N):
    ni = -1
    near = 0
    for j in range(i):
        if R[j]>near and A[j]<A[i]:
            ni = j
            near = R[j]
    if ni==-1:
        R[i] = 1
    else:
        R[i] = R[ni] + 1

for i in range(N-1,-1,-1):
    ni = -1
    near = 0
    for j in range(i+1,N):
        if S[j]>near and A[j]<A[i]:
            ni = j
            near = S[j]
    if ni==-1:
        S[i] = 1
    else:
        S[i] = S[ni] + 1

max = 0
for i in range(N):
    if R[i]+S[i]>max:
        max = R[i]+S[i]
print(max-1)