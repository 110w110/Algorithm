import sys

N, M = map(int, sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().split()))

# print(L)

result = 0

for i in L:
    for j in L:
        for k in L:
            if i==j or j==k or k==i:
                continue
            if result<=i+j+k and i+j+k<=M:
                result = i+j+k

print(result)
