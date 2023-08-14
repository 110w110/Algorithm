# 41m20s solved
from collections import deque

def BFS(x, y, B):
    X, Y = len(B[0]), len(B)
    visited = [[False for _ in range(X)] for _ in range(Y)]
    D = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    Q = deque()
    # 첫 위치, 0 push
    Q.append((x, y, 0))

    while Q:
        # print(Q)
        x, y, c = Q.popleft()
        # print(x,y,c)
        # 이미 방문했으면 continue
        if visited[y][x] is True:
            continue

        visited[y][x] = True

        # G면 return c
        if B[y][x] == 'G':
            return c

        # 상하좌우 중 갈 수 있는 위치와 c+1 push하고 visited 표시
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            while (0 <= nx < X) and (0 <= ny < Y):
                if B[ny][nx] == 'D':
                    Q.append((nx - dx, ny - dy, c + 1))
                    break
                elif (dx == 0 and (ny == 0 or ny == Y - 1)) or (dy == 0 and (nx == 0 or nx == X - 1)):
                    Q.append((nx, ny, c + 1))
                    break
                else:
                    nx, ny = nx + dx, ny + dy

    return -1


def solution(board):
    answer = 0
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[j][i] == 'R':
                return BFS(i, j, board)
                break
    return answer