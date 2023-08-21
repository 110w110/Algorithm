# 15m36s solved
def solution(pro, spd):
    answer = []
    state = [0 for _ in range(len(pro))]

    while True:
        c = True
        for p in pro:
            if p != 100:
                c = False
        if c == True:
            break

        for pi in range(len(pro)):
            pro[pi] = min(100, pro[pi] + spd[pi])
            if pro[pi] == 100 and state[pi] == 0:
                state[pi] = 1
        count = 0
        for si in range(len(state)):
            if state[si] == 0:
                break
            elif state[si] == 1:
                count += 1
                state[si] = 2
        if count != 0:
            answer.append(count)

    return answer