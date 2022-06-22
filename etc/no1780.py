import sys
sys.setrecursionlimit(10*9)

N = int(sys.stdin.readline())
P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
global result
result = [0,0,0]

def cut(x,y,r):
    d = r//3
    global result

    check = P[y][x]
    for i in range(r):
        for j in range(r):
            if P[y+i][x+j]!=check:
                for a in range(3):
                    for b in range(3):
                        cut(x+b*d,y+a*d,d)
                return
    result[check+1] += 1
    return

cut(0,0,N)
print(*result,sep="\n")