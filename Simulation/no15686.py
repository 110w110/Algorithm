import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = []
H = []
# print(N,M)
# print(*Map, sep='\n')

# 모든 치킨 집 좌표 뽑아내기
for j in range(N):
    for i in range(N):
        if Map[j][i] == 2:
            C.append((i,j))
        if Map[j][i] == 1:
            H.append((i,j))

# print(C)

# 조합으로 모든 경우의 수 돌리고 최소값 갱신하기
min_chicken = 1e9
for m in range(M):
    com = list(combinations(C,m+1))
    # print(com)
    # for문으로 모든 H 돌면서 모든 C와의 거리 중 최소 값을 누적합
    for cc in com:
        chicken = 0
        # print("cc",cc)
        for h in H:
            dist = 1e9
            for c in cc:
                if abs(h[0]-c[0]) + abs(h[1]-c[1]) < dist:
                    dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
                # print(h,c,dist)
            chicken += dist
        # print("min:",min_chicken)
        if chicken < min_chicken:
            min_chicken = chicken

print(min_chicken)