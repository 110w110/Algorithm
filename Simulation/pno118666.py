# 16m solved
def solution(survey, choices):
    answer = ''
    K = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        s = ''
        c = abs(choices[i] - 4)
        if choices[i] < 4:
            s = survey[i][0]
        else:
            s = survey[i][1]
        K[s] += c

    if K['R'] >= K['T']:
        answer += 'R'
    else:
        answer += 'T'

    if K['C'] >= K['F']:
        answer += 'C'
    else:
        answer += 'F'

    if K['J'] >= K['M']:
        answer += 'J'
    else:
        answer += 'M'

    if K['A'] >= K['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer