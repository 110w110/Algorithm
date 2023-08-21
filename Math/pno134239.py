# 19m15s solved
def solution(k, ranges):
    answer = []
    line = []

    def findW(k):
        count = 0
        line.append(k)
        while k > 1:
            if k % 2 == 0:
                k = int(k / 2)
            else:
                k = k * 3 + 1
            count += 1
            line.append(k)
        return count

    def square(line, a, b):
        if b <= 0:
            b = len(line) + b
        if a >= b:
            return -1.0
        s = 0
        for x in range(a, b - 1):
            y1, y2 = line[x], line[x + 1]
            s += (y1 + y2) / 2
        return s

    findW(k)

    for r1, r2 in ranges:
        answer.append(square(line, r1, r2))
    return answer