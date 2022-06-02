# 입력
# 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다.
# 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다.
# N극은 0, S극은 1로 나타나있다.
#
# 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다.
# 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다.
# 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다.
# 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
#
# 출력
# 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
#
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
#
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
#
# 7

import sys

gear = ['','','','']
gear[0] = sys.stdin.readline().strip()
gear[1] = sys.stdin.readline().strip()
gear[2] = sys.stdin.readline().strip()
gear[3] = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
R = []
for _ in range(N):
    g, r = map(int,sys.stdin.readline().split())
    R.append((g,r))

def rotate(g,r):
    if r == -1:
        gear[g] = gear[g][1:]+gear[g][0]
    elif r == 1:
        gear[g] = gear[g][-1]+gear[g][:-1]

def score(gear):
    return int(gear[0][0]) + 2 * int(gear[1][0]) + 4 * int(gear[2][0]) + 8 * int(gear[3][0])

for line in R:
    gear_number = line[0]-1
    rotatation = line[1]

    work = [(gear_number,rotatation)]

    i = gear_number
    while i > 0 :
        if gear[i-1][2] != gear[i][6]:
            work.append((i-1,(((i-1)%2)*2-1)*rotatation*((gear_number%2)*2-1)))
        else :
            break
        i -= 1
    i = gear_number
    while i < 3 :
        if gear[i][2] != gear[i+1][6]:
            work.append((i+1,(((i+1)%2)*2-1)*rotatation*((gear_number%2)*2-1)))
        else :
            break
        i += 1

    for j in work: rotate(j[0],j[1])

print(score(gear))