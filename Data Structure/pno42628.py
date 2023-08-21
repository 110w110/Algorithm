# 12m15s solved
from collections import deque
def solution(operations):
    answer = []
    Q = deque()

    for o in operations:
        op, n = o.split()
        n = int(n)
        if op == 'I':
            i = 0
            while i < len(Q):
                if Q[i] >= n:
                    break
                i += 1
            if i == len(Q):
                Q.append(n)
            else:
                Q.insert(i, n)
        elif n == 1 and len(Q) != 0:
            Q.pop()
        elif n == -1 and len(Q) != 0:
            Q.popleft()

    if len(Q) == 0:
        return [0, 0]
    return [Q[-1], Q[0]]