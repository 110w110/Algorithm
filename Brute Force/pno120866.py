# 8m50s solved
def solution(board):
    answer = 0
    bomb = []
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[j][i] == 1:
                bomb.append((i, j))

    D = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for bx, by in bomb:
        for dx, dy in D:
            nx, ny = bx + dx, by + dy
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                if board[ny][nx] == 0:
                    board[ny][nx] = 2

    for b in board:
        for c in b:
            if c == 0:
                answer += 1

    return answer