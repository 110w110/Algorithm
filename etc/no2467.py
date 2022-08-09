import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
R = list(map(int,sys.stdin.readline().split()))
s = 0
t = N-1

global min, ms, mt
min = 10**12
ms = s
mt = t

def mix(a,b):
    global min, ms, mt
    if a>=b:
        return
    if abs(R[a]+R[b])<=min:
        ms = a
        mt = b
        min = abs(R[b]+R[a])
    if abs(a)==abs(b):
        return
    elif abs(R[b-1]+R[a])==abs(R[b]+R[a+1]):
        mix(a,b-1)
        mix(a+1,b)
    elif abs(R[b-1]+R[a])>abs(R[b]+R[a+1]):
        mix(a+1,b)
    else:
        mix(a,b-1)

mix(s,t)
print(R[ms],R[mt])