#16m28s solved
def solution(N, road, K):
    answer = 0
    T = [[10 ** 9] * N for _ in range(N)]

    for a, b, c in road:
        T[a - 1][b - 1], T[b - 1][a - 1] = min(c, T[a - 1][b - 1]), min(c, T[b - 1][a - 1])

    for m in range(N):
        for j in range(N):
            for i in range(N):
                if i == j:
                    T[i][i] = 0
                    continue
                if T[j][i] > T[j][m] + T[m][i]:
                    T[j][i] = T[j][m] + T[m][i]

    # print(*T, sep='\n')
    for x in T[0]:
        if x <= K:
            answer += 1
    return answer