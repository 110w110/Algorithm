import sys

N, B = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def mul(X,N):
    n = N//2
    if N%2==0:
        #A^n A^n
        if n==1:
            return X
        elif n==0:
            return X
        else:
            X = mul(X,n)
            R = X
            
    else:
        #A^n A^n A


print(*A,sep='\n')