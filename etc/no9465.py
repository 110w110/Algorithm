import sys

T = int(sys.stdin.readline())
R = []
for _ in range(T):
    n = int(sys.stdin.readline())
    P = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]

    if n>=3:
        #위에서 시작
        r1 = P[0][0]
        x, y = 0, 0
        while x<=n-2:
            if y==0:
                if x>=n-2:
                    r1 += P[1][x+1]
                    y = 1
                else:
                    if P[1][x+1] + P[0][x+2] >= P[1][x+2]:
                        r1 += P[1][x+1] + P[0][x+2]
                        y = 0
                    else:
                        r1 += P[1][x+2]
                        y = 1
            else:
                if x>=n-2:
                    r1 += P[0][x+1]
                    y = 0
                else:
                    if P[0][x+1] + P[1][x+2] >= P[0][x+2]:
                        r1 += P[0][x+1] + P[1][x+2]
                        y = 1
                    else:
                        r1 += P[0][x+2]
                        y = 0
            x += 2
            # print("r1:",r1)

        #아래에서 시작
        r2 = P[1][0]
        x, y = 0, 1
        while x <= n-2:
            if y == 0:
                if P[1][x + 1] + P[0][x + 2] >= P[1][x + 2]:
                    r2 += P[1][x + 1] + P[0][x + 2]
                    y = 0
                else:
                    r2 += P[1][x + 2]
                    y = 1
            else:
                if P[0][x + 1] + P[1][x + 2] >= P[0][x + 2]:
                    r2 += P[0][x + 1] + P[1][x + 2]
                    y = 1
                else:
                    r2 += P[0][x + 2]
                    y = 0
            x += 2
            # print("r2:",r2)

        R.append(max(r1, r2))
    elif n==2:
        R.append(max(P[0][0]+P[1][1],P[1][0]+P[0][1]))
    else:
        R.append(max(P[0][0],P[1][0]))


print(*R,sep='\n')