import sys
sys.setrecursionlimit(10**9)

N, B = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def mul(A,B):
    result = [[0 for _ in range(len(B))] for _ in range(len(A))]
    for r in range(len(B)):
        for c in range(len(A)):
            t = 0
            for i in range(len(A)):
                t += A[r][i] * B[i][c]
            result[r][c] = t % 1000
    return result

def sep(X,N):
    if N==1:
        for r in range(len(X)):
            for c in range(len(X)):
                X[r][c] %= 1000
        return X
    n = N//2
    if N%2==0:
        tmp = sep(X,n)
        return mul(tmp,tmp)
    else:
        tmp = sep(X,n)
        return mul(mul(tmp,tmp),X)

R = sep(A,B)
for x in range(len(R)):
    print(*R[x],sep=' ')