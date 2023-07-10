"""
바이러스 최대로 퍼뜨려서 안전구역 계산하는 함수 safeZone()
 -> 내부는 DFS로? BFS로? DFS로 일단 해보자 구현이 더 간단할듯

1. 입력받기
2. 모든 0이 존재하는 칸 탐색해서 모아두기 (Z)
3. Z 중 3개를 뽑는 조합 combinations?
4. 조합 경우의 수 마다 safeZone() 실행해서 최대값 갱신
"""

# 39 min solved
from itertools import *
import sys
import copy

N, M = map(int, sys.stdin.readline().split())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def DFS(v, T, N, M, visited):
    x, y = v
    T[y][x] = 2
    D = [(0,1),(0,-1),(1,0),(-1,0)] # 하 상 우 좌
    for d in D:
        dx, dy = x + d[0], y + d[1]
        if (0 <= dx < M) and (0 <= dy < N):
            if visited[dy][dx] == 0 and T[dy][dx] == 0:
                visited[dy][dx] = 1
                DFS((dx,dy),T,N,M,visited)

def safeZone(T, C, V, N, M):
    zone = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    T_copied = copy.deepcopy(T)
    for cx, cy in C:
        T_copied[cy][cx] = 1
    for v in V:
        DFS(v,T_copied,N,M,visited)
    for j in range(N):
        for i in range(M):
            if T_copied[j][i] == 0:
                zone += 1
    return zone

Z = []
V = []
result = 0
for j in range(N):
    for i in range(M):
        if T[j][i] == 0:
            Z.append((i,j))
        elif T[j][i] == 2:
            V.append((i,j))

C = list(combinations(Z,3))

for c in C:
    s = safeZone(T, c, V, N, M)
    if s > result:
        result = s

print(result)

"""
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
입력

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.
출력

첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다."""