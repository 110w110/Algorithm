# 27m21s solved
def solution(n, s, a, b, fares):
    answer = 1e9

    F = [[1e9 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for x, y, f in fares:
        F[y - 1][x - 1] = f
        F[x - 1][y - 1] = f
    # print(*F, sep='\n')

    # 플로이드워셜
    for m in range(n):
        for i in range(n):
            for j in range(n):
                F[i][j] = min(F[i][j], F[i][m] + F[m][j])

    # print(*F, sep='\n')

    # 경유지 합승 최소 갱신
    for k in range(n):
        answer = min(answer, F[s - 1][k] + F[k][a - 1] + F[k][b - 1])

    return answer


"""
S 플로이드 워셜
특정 경유지까지 합승하는 경우 모두 탐색해서 최소값 찾기
"""