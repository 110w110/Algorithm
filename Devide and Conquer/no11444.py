import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

def mul(A,B):
    result = [[0 for _ in range(len(B))] for _ in range(len(A))]
    for r in range(len(B)):
        for c in range(len(A)):
            t = 0
            for i in range(len(A)):
                t += A[r][i] * B[i][c]
            result[r][c] = t % 1000000007
    return result

def sep(X,N):
    if N==0:
        return [[1]]
    if N==1:
        for r in range(len(X)):
            for c in range(len(X)):
                X[r][c] %= 1000000007
        return X
    n = N//2
    tmp = sep(X,n)
    if N%2==0:
        return mul(tmp,tmp)
    else:
        return mul(mul(tmp,tmp),X)

print(sep([[1,1],[1,0]],n-1)[0][0])
