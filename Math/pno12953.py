# 13m7s solved
from itertools import combinations
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, (a % b))

def LCM(a, b):
    return int(a * b / GCD(a,b))

def solution(arr):
    answer = arr.pop()
    while arr:
        k = arr.pop()
        answer = LCM(answer,k)
    return answer