# 28m40s solved
from collections import deque

def solution(places):
    answer = []

    def bfs(p, T):
        px, py = p
        visited = [[False for _ in range(5)] for _ in range(5)]
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Q = deque()
        Q.append((px, py, 0))

        while Q:
            qx, qy, depth = Q.popleft()
            visited[qy][qx] = True
            for dx, dy in D:
                nx, ny = qx + dx, qy + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and depth < 2 and visited[ny][nx] == False:
                    if T[ny][nx] == 'P' and depth < 2:
                        return 0
                    if T[ny][nx] == 'O' and depth < 2:
                        Q.append((nx, ny, depth + 1))
        return 1

    def exe(T):
        P = deque()
        for j in range(5):
            for i in range(5):
                if T[j][i] == 'P':
                    P.append((i, j))
        for p in P:
            if bfs(p, T) == 0:
                return 0
        return 1

    for p in places:
        answer.append(exe(p))

    return answer