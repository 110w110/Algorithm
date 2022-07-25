import sys

N = int(sys.stdin.readline())
R = list(map(int,sys.stdin.readline().split()))
s = 0
t = N-1
min = 10**9
ms, mt = s,t

while True:
    if s>=t-1:
        break
    print(R[s],R[t])
    if abs(R[t]+R[s])<min:
        min = abs(R[t]+R[s])
        ms, mt = s, t

    if abs(s)==abs(t):
        break
    elif abs(R[t-1]+R[s])<abs(R[t]+R[s+1]):
        t-=1
    else:
        s+=1

print(R[ms], R[mt], abs(R[mt]+R[ms]))