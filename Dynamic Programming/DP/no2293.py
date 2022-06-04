import sys

n, k = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
result = [0 for _ in range(k+1)]
result[0] = 1

coins.sort()

for coin in coins:
    for i in range(1,k+1):
        if i>=coin:
            result[i]+=result[i-coin]

print(result[k])
