# 3m20s solved
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for j in range(len(arr1)):
        for i in range(len(arr2[0])):
            t = 0
            for k in range(len(arr1[0])):
                t += arr1[j][k] * arr2[k][i]
            answer[j][i] = t

    return answer