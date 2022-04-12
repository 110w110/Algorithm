# 동전1 :: 2293
# 문제
# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
# 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
# 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
#
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
#
# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
# 다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
# 동전의 가치는 100,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.
#
# 3 10
# 1
# 2
# 5
import sys


def f(k, v):
    args = v[:]
    args.append(k)
    args = tuple(args)
    # print(args)
    if args in mem:
        # print("mem")
        return mem[args]

    if k == 0:
        return 1
    if len(v) == 0:
        return 0

    x = v[-1]
    result = 0
    for i in range(int(k/x)+1):
        result += f(k-x*(i),v[:-1])
        # 5 - 5*1
        # print(k-x*(i+1),v[:-1])

    # print(k,v,result)
    mem[args]=result
    return result

n, k = map(int, input().split())
v = []
mem = {}
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp <= k:
        v.append(tmp)

v.sort()
if len(v)==0:
    print(0)
else:
    print(f(k,v))

# 5 [1,2]
# 1,1,1,1,1 1로 5만들기 = 1
# 1,1,1,2   1로 3만들기 = 1
# 1,2,2     1로 1만들기 = 1