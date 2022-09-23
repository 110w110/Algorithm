# k진수에서 소수 개수 구하기
import math


def primeNumber(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    r = 0
    s = 1
    while True:
        if n < (k ** s):
            break
        s += 1
    print(s, n, k ** s)
    while s >= 0:
        t = (n // (k ** s))
        r += (n // (k ** s)) * (10 ** s)
        n = (n % (k ** s))
        s -= 1
        print(t, r, s, n)
    print(r)

    L = str(r).split('0')
    print(L)

    for l in L:
        if l != '':
            if primeNumber(int(l)):
                print(int(l), primeNumber(int(l)))
                answer += 1
    return answer