import sys

N = int(sys.stdin.readline())
P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

global count
count = 0

def f(px,py,x,y):
    print('(',px,',',py,') (',x,',',y,')')
    if x==N-1 and y==N-1:
        global count
        count += 1
        print("======",count)
    # 현재 가로일 때 -> py==y
    # x>=N-1이면 넘어가
    # 가로, 대각선 체크
    if py==y and x<N-1:
        if P[y][x+1]==0:
            if y<N-1:
                if P[y+1][x+1]==0 and P[y+1][x]==0:
                    f(x,y,x+1,y+1)
                f(x,y,x+1,y)
            else:
                f(x,y,x+1,y)

    # 현재 세로일 때 -> px==x
    # y>=N-1이면 넘어가
    # 세로, 대각선 체크
    elif px==x and y<N-1:
        if P[y+1][x]==0:
            if x<N-1:
                if P[y+1][x+1]==0 and P[y][x+1]==0:
                    f(x,y,x+1,y+1)
                    f(x,y,x,y+1)
            else:
                f(x,y,x,y+1)

    # 현재 대각선일 때 -> else
    # x>=N-1 or y>=N-1이면 넘어가
    # 가로, 세로, 대각선 체크
    elif px!=x and py!=y:
        if x<N-1 and y<N-1:
            if P[y][x+1]==0:
                if P[y+1][x]==0:
                    if P[y+1][x+1]==0:
                        f(x,y,x+1,y+1)
        if x<N-1:
            if P[y][x+1]==0:
                f(x,y,x+1,y)
        if y<N-1:
            if P[y+1][x]==0:
                f(x,y,x,y+1)

        #


f(0,0,1,0)
print(count)

# print(*P,sep='\n')