# 15m10s solved
def check(arr, x, y, size):
    if size == 1:
        return [1, 0] if arr[y][x] == 0 else [0, 1]
    s = [0, 0]

    # 4등분해서 재귀호출하고 값 누적
    nsize = int(size / 2)
    a = check(arr, x, y, nsize)
    b = check(arr, x + nsize, y, nsize)
    c = check(arr, x, y + nsize, nsize)
    d = check(arr, x + nsize, y + nsize, nsize)
    s[0] = a[0] + b[0] + c[0] + d[0]
    s[1] = a[1] + b[1] + c[1] + d[1]

    # 한쪽 값이 0이면 반대쪽값/4 해서 리턴
    if s[0] == 0:
        return [0, int(s[1] / 4)]
    elif s[1] == 0:
        return [int(s[0] / 4), 0]
    return s


def solution(arr):
    answer = check(arr, 0, 0, len(arr[0]))
    return answer