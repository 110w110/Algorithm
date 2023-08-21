# 16m35s solved
def solution(elements):
    E = elements + elements
    S = []

    for l in range(1, len(elements) + 1):
        for s in range(0, len(elements)):
            S.append(sum(E[s:s + l]))

    return len(set(S))