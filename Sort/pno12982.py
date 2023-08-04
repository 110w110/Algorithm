# 1m55s solved
def solution(D, budget):
    answer = 0
    D.sort()
    current = 0
    for d in D:
        if current + d <= budget:
            current += d
            answer += 1
    return answer