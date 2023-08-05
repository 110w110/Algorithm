# 3m32s solved
def solution(arr):
    answer = []
    p = -1
    for i in range(len(arr)):
        a = arr[i]
        if a != p:
            answer.append(a)
        p = a
    return answer