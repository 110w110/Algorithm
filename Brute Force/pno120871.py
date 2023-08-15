# 13m10s solved
def solution(n):
    answer = 0
    for x in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in list(str(answer)):
            answer += 1
    return answer