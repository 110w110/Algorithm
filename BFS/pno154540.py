# BFS로 풀거야
# 일단 가장 바깥 반복문은 좌상단부터 우하단까지 돌면서 X가 아닌 원소를 찾으면 큐에 넣고 BFS 시작
# 큐가 종료되면 지금까지 합을 answer에 append하고 다른 X가 아닌 섬 찾아서 계속 돌기
#
# BFS에 들어가면 내 값을 누적합에 더하고 나는 X로 바꿈 (visited 대신)
# 상하좌우에 X가 아닌 값이 있으면 Q에 넣음
# 27 min solved

from collections import deque


def BFS(M, Q, x, y):
    value = M[y][x]
    if value == 'X':
        return 0
    M[y][x] = 'X'
    D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for d in D:
        ny, nx = y + d[0], x + d[1]
        if 0 <= ny < len(M) and 0 <= nx < len(M[0]):
            if M[ny][nx] != 'X':
                Q.append((nx, ny))
    return int(value)


def solution(maps):
    answer = []
    M = [list(i) for i in maps]

    for j in range(len(M)):
        for i in range(len(M[0])):
            if M[j][i] == 'X':
                continue
            Q = deque()
            Q.append((i, j))
            count = 0
            while Q:
                q = Q.popleft()
                count += BFS(M, Q, q[0], q[1])
            answer.append(count)

    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

#  무인도 여행
#
# 문제 설명
#
# 메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다. 지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다. 지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며, 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다. 이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다. 어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 합니다.
#
# 지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요. 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.
# 제한사항
#
#     3 ≤ maps의 길이 ≤ 100
#         3 ≤ maps[i]의 길이 ≤ 100
#         maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열입니다.
#         지도는 직사각형 형태입니다.
#
# 입출력 예
# maps 	result
# ["X591X","X1X5X","X231X", "1XXX1"] 	[1, 1, 27]
# ["XXX","XXX","XXX"] 	[-1]