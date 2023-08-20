# 15m20s solved
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0, words))

    def bfs(a, b, depth, words):
        if a == b:
            return depth
        for w in words:
            count = 0
            for i in range(len(w)):
                if w[i] != a[i]:
                    count += 1
            if count == 1:
                words.remove(w)
                q.append((w, depth + 1, words))

    while q:
        qi, d, w = q.popleft()
        answer = bfs(qi, target, d, w)

    return answer if answer is not None else 0