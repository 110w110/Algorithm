import sys

t = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(t)]

dp = [1,2,4]

for i in range(3,max(l)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for j in range(t):
    print(dp[l[j]-1])