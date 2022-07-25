import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
D = {}
S = {}

def dp(N):
    if N in D:
        return D[N]
    if N==0:
        return 10**9
    if N==1:
        return 0
    if N//3 not in D and N//3>=0:
        D[N//3] = dp(N//3)
    if N//2 not in D and N//2>=0:
        D[N//2] = dp(N//2)
    if N-1 not in D:
        D[N-1] = dp(N-1)

    a,b,c = 10**9, 10**9, 10**9
    if N%3==0:
        a = D[N//3]
    if N%2==0:
        b = D[N//2]
    if N-1>1:
        c = D[N-1]

    m = min(a,b,c)
    if m==a:
        S[N] = N//3
        return a + 1
    elif m==b:
        S[N] = N//2
        return b + 1
    else:
        S[N] = N-1
        return c + 1

def ans(N):
    print(N,end=' ')
    if N==1:
        return
    ans(S[N])

print(dp(N))
ans(N)