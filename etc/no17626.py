import sys
sys.setrecursionlimit(5000000)

dp = [5 for _ in range(50001)]
n = int(sys.stdin.readline())

def d(i):
    if i <= 1:
        return i
    elif i**0.5 - int(i**0.5) == 0.0:
        return 1
    else:
        for j in range(1,int(i**0.5)+1):
            a = dp[i]
            b = dp[j * j]
            c = dp[i - j * j]
            if a == 5:
                a = 4
            if b == 5:
                b = d(j*j)
            if c == 5:
                c = d(i-j*j)
            dp[i]=min(a,b+c)
        return dp[i]

    # for i in range(2, n + 1):
    #     if i ** 0.5 - int(i ** 0.5) == 0.0:
    #         dp[i] = 1
    #     else:
    #         for j in range(1, int(i ** 0.5) + 1):
    #             dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

# dp[0]=0
# dp[1]=1
# for i in range(2,n+1):
#     if i**0.5-int(i**0.5)==0.0:
#         dp[i]=1
#     else:
#         for j in range(1,int(i**0.5)+1):
#             dp[i] = min(dp[i], dp[j*j]+dp[i-j*j])


print(d(n))



