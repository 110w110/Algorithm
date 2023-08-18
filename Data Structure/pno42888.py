# 5m27s solved
def solution(record):
    answer = []
    D = {}
    for r in record:
        c = r.split()
        if c[0] != 'Leave':
            D[c[1]] = c[2]

    for r in record:
        c = r.split()
        if c[0] == 'Enter':
            answer.append(D[c[1]] + "님이 들어왔습니다.")
        elif c[0] == 'Leave':
            answer.append(D[c[1]] + "님이 나갔습니다.")

    return answer