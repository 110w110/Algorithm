import sys
sys.setrecursionlimit(10*2000)

I = []
while True:
    try:
        I.append(int(sys.stdin.readline()))
    except:
        break

# I = list(map(int,sys.stdin.readline().split()))
T = {}

def f(P):
    if len(P)==1:
        T[P[0]] = -1,-1
        return
    elif len(P)==0:
        return
    M = P[0]
    i = 1
    while i<len(P):
        if M<=P[i]:
            break
        i += 1
    L = P[1:i]
    R = P[i:]
    if len(L)!=0:
        if len(R)!=0:
            T[M] = L[0], R[0]
        else:
            T[M] = L[0], -1
    else:
        if len(R)!=0:
            T[M] = -1, R[0]
        else:
            T[M] = -1, -1

    # print(M,L,R)
    if len(L)!=0:
        f(L)
    if len(R)!=0:
        f(R)

f(I)
# print(T)

def postorder(v):
    if v==-1:
        return
    postorder(T[v][0])
    postorder(T[v][1])
    print(v)

postorder(I[0])