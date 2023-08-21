# 38m12s solved
def solution(n):
    m, c = 0, 0
    for l in range(31):
        if 2 ** l > n:
            m = l
            break

    while m >= 0:
        # print(m)
        if (n - 2 ** m) >= 0:
            n -= 2 ** m
            c += 1
            # print(n, 'c=',c)
        m -= 1

    return c + n