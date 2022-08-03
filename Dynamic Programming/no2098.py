import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
R = [[None for _ in range(1<<N)] for _ in range(N)]
# print(*W,sep='\n')

def tsp(node,path):
    # print(node,bin(path))
    # 모두 방문했으면 리턴
    # 메모이제이션 되어있다면 그 값 리턴
    # 그렇지 않으면 모든 남은 노드를 향해 재귀적으로 거리 계산 후 리턴

    # 모두 방문했으면 리턴
    if path==(1<<N)-1:
        return W[node][0] or 10**9
    # 메모이제이션 되어있다면 그 값 리턴
    if R[node][path] is not None:
        return R[node][path]
    # 그렇지 않으면 모든 남은 노드를 향해 재귀적으로 거리 계산 후 리턴
    tmp = 10**9
    for n in range(N):
        if path & (1 << n) == 0 and W[node][n] != 0:
            tmp = min(tmp, tsp(n,path|(1<<n)) + W[node][n])
    R[node][path]=tmp
    return tmp

print(tsp(0,1))