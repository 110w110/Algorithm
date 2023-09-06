# 6m20s solved
from collections import Counter
def solution(k, tangerine):
    answer = 0
    C = Counter(tangerine).most_common()
    count = 0
    for c in C:
        answer += 1
        count += c[1]
        if count >= k:
            break
    return answer
