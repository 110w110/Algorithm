import sys
import copy

global count, max, S, P

N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
check_num = [False for _ in range(N)]
check_up = [False for _ in range(N*2)]
check_down = [False for _ in range(N*2)]

count = 0
max = 0

P = copy.deepcopy(S)

def nbishop(x,y):
    global count, max, S, P
    # if y>=N:
    #     print('='*10)
    #     if count>max:
    #         max = count
    #     count = 0
    #     return
    if P[y][x]==0:
        return

    for i in range(N):
        for j in range(N):
            if i*N+j<=y*N+x:
                continue
            if P[i][j]==0:
                continue
            if i+j==y+x:
                continue
            if i-j==y-x:
                continue
            nbishop(j,i)
            print(x,y,'->',j,i,'c =',count)
            count += 1
            P[j][i] = 2

    print('=' * 10)
    if count > max:
        max = count
    count = 0
    P = copy.deepcopy(S)


    # global count
    # if y>=N:
    #     count += 1
    #     return
    #
    # for x in range(N):
    #     if check_num[x]:
    #         continue
    #     if check_up[x+y]:
    #         continue
    #     if check_down[x-y+N]:
    #         continue
    #
    #     check_num[x] = True
    #     check_up[x+y] = True
    #     check_down[x-y+N] = True
    #
    #     nbishop(y+1)
    #
    #     check_num[x] = False
    #     check_up[x+y] = False
    #     check_down[x-y+N] = False

for a in range(N):
    for b in range(N):
        if P[a][b]==1:
            nbishop(a,b)
print(max)