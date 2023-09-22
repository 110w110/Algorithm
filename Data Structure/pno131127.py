from collections import Counter
def solution(want, number, discount):
    answer = 0
    cwant = []
    for i in range(len(want)):
        cwant += [want[i]] * number[i]
    cwant = Counter(cwant)

    for i in range(len(discount) - 9):
        flag = False
        temp = Counter(discount[i:i + 10])
        for x in cwant:
            if x not in temp:
                flag = True
                break
            elif temp[x] < cwant[x]:
                flag = True
                break

        if flag == False:
            answer += 1

    return answer