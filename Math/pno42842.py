# 8m24s solved
def solution(brown, yellow):
    answer = []
    hw = int((brown - 4) / 2)

    for k in range(1, hw):
        h = hw - k + 2
        w = k + 2
        if h > w:
            continue
        y = (h - 2) * (w - 2)
        if y == yellow:
            return [w, h]
    return answer