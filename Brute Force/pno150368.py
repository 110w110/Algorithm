# 32m20s solved
from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    discount = [10, 20, 30, 40]
    cases = list(product(discount, repeat=len(emoticons)))

    for c in cases:
        d = [round((1 - c[i] * 0.01) * emoticons[i]) for i in range(len(emoticons))]
        result = [0, 0]

        for u in users:
            s = 0
            for ei in range(len(emoticons)):
                if c[ei] >= u[0]:
                    s += d[ei]
            if s >= u[1]:
                result[0] += 1
            else:
                result[1] += s

        if result[0] > answer[0] or (result[0] == answer[0] and result[1] > answer[1]):
            answer = result

    return answer