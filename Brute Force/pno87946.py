# 3m15s solved
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    P = list(permutations(dungeons))

    for p in P:
        count = 0
        ck = k
        for pp in p:
            if pp[0] > ck:
                break
            count += 1
            ck -= pp[1]
        answer = max(answer, count)

    return answer