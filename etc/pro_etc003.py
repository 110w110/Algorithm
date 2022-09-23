import math


def strToTime(t):
    a, b = t.split(":")
    return int(a) * 60 + int(b)


def solution(fees, records):
    answer = []

    A = dict()

    for line in records:
        timeStr, number, detail = line.split()
        time = strToTime(timeStr)
        # print(number, time, detail)
        # print(time, number, detail)
        if number not in A:
            A[number] = [time, detail, 0]
        elif detail == "OUT":
            prev = A[number]
            A[number] = [time, detail, prev[2] + time - prev[0]]
        elif detail == "IN":
            prev = A[number]
            A[number] = [time, detail, prev[2]]
        else:
            print("error case")

    for a in A:
        # print(a, A[a])
        if A[a][1] == "IN":
            A[a][2] += 23 * 60 + 59 - A[a][0]
            A[a][1] = "OUT"
            A[a][0] = 23 * 60 + 59

    print(A)

    for i in sorted(A.items()):
        print(i)
        extra_time = A[i[0]][2] - fees[0]
        extra_fee = 0
        if extra_time > 0:
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]

        answer.append(fees[1] + extra_fee)

    return answer

# fees  0       1       2       3
#       기본시간  기본요금  단위시간   단위요금
#
# records 시각 차량번호 내역