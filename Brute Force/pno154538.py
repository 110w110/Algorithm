def solution(x, y, n):
    answer = 0
    # 연산 횟수별로 리스트에 튜플로 계속 담아서 올리는데 y를 넘어서는건 안넣고 계속 시도?
    # 모든 값이 넘어가서 다음 튜플에 넣는 값이 없으면 -1
    # 튜플 값 중에 y가 있으면 인덱스 값 출력?

    L = [[x]]
    if x == y:
        return 0

    for l in L:
        answer += 1
        tmp = []
        for k in l:
            if k * 2 == y or k * 3 == y or k + n == y:
                return answer
            if k * 2 < y:
                tmp.append(k * 2)
            if k * 3 < y:
                tmp.append(k * 3)
            if k + n < y:
                tmp.append(k + n)
        if len(tmp) == 0:
            answer = -1
        else:
            L.append(set(tmp))

    return answer

# 숫자 변환하기
# 문제 설명
# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.
#
# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.
# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.
#
# 제한사항
# 1 ≤ x ≤ y ≤ 1,000,000
# 1 ≤ n < y
# 입출력 예
# x	y	n	result
# 10	40	5	2
# 10	40	30	1
# 2	5	4	-1
# 입출력 예 설명
# 입출력 예 #1
# x에 2를 2번 곱하면 40이 되고 이때가 최소 횟수입니다.
#
# 입출력 예 #2
# x에 n인 30을 1번 더하면 40이 되고 이때가 최소 횟수입니다.
#
# 입출력 예 #3
# x를 y로 변환할 수 없기 때문에 -1을 return합니다.