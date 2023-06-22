from collections import deque
import sys

def BFS(Maze, R, C):
    Q = deque()
    Q.append((0,0))
    visited = [[False for _ in range(C)] for _ in range(R)]
    answer = [[1e9 for _ in range(C)] for _ in range(R)]
    answer[0][0] = 1

    while Q:
        (qx, qy) = Q.popleft()

        # 상하좌우 중에 방문하지 않은 좌표 큐에 넣기
        if (0 < qx) and visited[qy][qx - 1] == False:
            if Maze[qy][qx - 1] == '1':
                Q.append((qx - 1,qy))
                answer[qy][qx - 1] = answer[qy][qx] + 1
                visited[qy][qx - 1] = True
        if (qx < C -1) and visited[qy][qx + 1] == False:
            if Maze[qy][qx + 1] == '1':
                Q.append((qx + 1, qy))
                answer[qy][qx + 1] = answer[qy][qx] + 1
                visited[qy][qx + 1] = True
        if (0 < qy) and visited[qy - 1][qx] == False:
            if Maze[qy - 1][qx] == '1':
                Q.append((qx,qy - 1))
                answer[qy - 1][qx] = answer[qy][qx] + 1
                visited[qy - 1][qx] = True
        if (qy < R -1) and visited[qy + 1][qx] == False:
            if Maze[qy + 1][qx] == '1':
                Q.append((qx, qy + 1))
                answer[qy + 1][qx] = answer[qy][qx] + 1
                visited[qy + 1][qx] = True

    return answer[R-1][C-1]

R, C = map(int, sys.stdin.readline().split())
Maze = [list(sys.stdin.readline().split()[0]) for _ in range(R)]

print(BFS(Maze, R, C))