# 34m20s solved
import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)

def DFS(i, W, visited):
    count = 1
    visited[i] = True
    for w in range(len(W[i])):
        if W[i][w] == 1 and visited[w] is False:
            count += DFS(w, W, visited)
    return max(1, count)

def solution(n, wires):
    answer = 1e9
    """
    전체 개수 n
    트리의 모든 간선 전체 반복문
        1. 간선 제거
        2. 어떤 노드에서 연결된 모든 노드 개수 카운트 (DFS or BFS)
        3. n - 개수 로 반대 트리 개수 확인
        4. 두 값의 절대값 차이의 최소를 갱신
    최종 최소값 리턴
    """
    W = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in wires:
        W[a - 1][b - 1] = 1
        W[b - 1][a - 1] = 1

    # print(*W, sep='\n')
    # print(DFS(0,W,[False]*len(W[0])))

    for a, b in wires:
        N = deepcopy(W)
        N[a - 1][b - 1] = 0
        N[b - 1][a - 1] = 0
        k = DFS(0, N, [False] * len(N[0]))
        answer = min(answer, abs(k - (n - k)))

    return answer