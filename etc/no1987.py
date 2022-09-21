import sys
sys.setrecursionlimit(10**9)
R, C = map(int, sys.stdin.readline().split())
T = [sys.stdin.readline() for _ in range(R)]
D = [(0,1),(0,-1),(1,0),(-1,0)]
# mem = []
# print(*T,sep='\n')
def find(x,y,mem):
    # 남은 갈 수 있는 모든 방향으로 재귀호출하여 그 값 중 최대값에 +1 하여 리턴
    # 갈 수 있는 길이 더 이상 없으면 1을 반환
    # print(1<<(ord(T[y][x])-65) & mem)

    M = 0
    for d in D:
        dy = y + d[1]
        dx = x + d[0]
        # print(dx,dy, mem, M+1, 1<<(ord(T[y][x])-65),1<<(ord(T[y][x])-65) & mem,1<<(ord(T[y][x])-65) | mem)
        if 0<= dx < C and 0 <= dy < R:
            if 1<<(ord(T[dy][dx])-65) & (1<<(ord(T[y][x])-65) | mem) == 0:
                tmp = find(dx,dy,1<<(ord(T[y][x])-65) | mem)
                if tmp > M:
                    M = tmp
    return 1 + M

print(find(0,0,0))