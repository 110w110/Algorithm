# 1916 최소비용 구하기
# 문제
# N개의 도시가 있다.
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라.
# 도시의 번호는 1부터 N까지이다.
#
# 입력
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
# 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다.
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다.
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
#
# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
# 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
#
# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
#
# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5
#
# 4

import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
E = [[] for _ in range(N)]
Dist = [int(1e9) for _ in range(N)]
Visit = [False for _ in range(N)]

for _ in range(M):
    s, d, w = map(int, sys.stdin.readline().split())
    E[s-1].append((d,w))

S, D = map(int, sys.stdin.readline().split())

route = [0 for _ in range(N)]

def Dijk(node):
    Visit[node] = True
    # route.append(node+1)

    # 인접노드 거리 갱신
    for W in E[node]:
        if Dist[W[0]-1] > W[1]+Dist[node]:
            Dist[W[0]-1] = W[1] + Dist[node]
            route[W[0]-1] = node+1
        # Dist[W[0]-1] = min(Dist[W[0]-1],W[1]+Dist[node])

    print(Dist)
    print(Visit)
    print(route)
    # 방문하지 않은 노드 중 가장 가까운 노드 선택
    m = 1e9
    isDone = True
    for i in range(1,N):
        if Dist[i] < m and Visit[i] == False:
            m = Dist[i]
            node = i
            isDone = False

    if isDone: return
    print(node)
    Dijk(node)

Dist[S-1] = 0
Dijk(S-1)
print(Dist[D-1])
print(Dist)
print(route)