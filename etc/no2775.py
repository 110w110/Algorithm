import sys
def f(K,N):
    if K == 0:
        return N
    else:
        result = 0
        for i in range(N):
            result += f(K-1,i+1)
        return result

t = int(sys.stdin.readline().strip())
r = []
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    r.append(f(k,n))

for _ in range(len(r)):
    print(r[_])