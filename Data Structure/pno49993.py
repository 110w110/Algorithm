# 7m20s solved
def solution(skill, sts):
    answer = 0

    for t in sts:
        l = list(filter(lambda x: x in skill, list(t)))
        answer += 1
        for li in range(len(l)):
            if l[li] != skill[li]:
                answer -= 1
                break

    return answer