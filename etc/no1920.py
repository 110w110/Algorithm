import sys

def bs(x,s,t):
    if t-s<1:
        print(0)
        return
    m = int((s+t)/2)
    if x == I[m]:
        print(1)
        return
    elif x < I[m]:
        bs(x,s,m)
    else:
        bs(x,m+1,t)

n = int(sys.stdin.readline().strip())
I = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
J = list(map(int,sys.stdin.readline().split()))

I.sort()
for x in J:
    bs(x,0,len(I))

