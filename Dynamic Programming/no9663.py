import sys

N = int(sys.stdin.readline())
check_num = [False for _ in range(N)]
check_up = [False for _ in range(N*2)]
check_down = [False for _ in range(N*2)]

global count
count = 0

def nqueen(y):
    global count
    if y>=N:
        count += 1
        return

    for x in range(N):
        if check_num[x]:
            continue
        if check_up[x+y]:
            continue
        if check_down[x-y+N]:
            continue

        check_num[x] = True
        check_up[x+y] = True
        check_down[x-y+N] = True

        nqueen(y+1)

        check_num[x] = False
        check_up[x+y] = False
        check_down[x-y+N] = False

nqueen(0)
print(count)