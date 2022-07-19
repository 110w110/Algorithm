import sys

n = int(sys.stdin.readline())
T = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

if len(T)==1:
    print(T[0][0])
else:
    pt = T[-1]
    for i in range(len(T)-1,-1,-1):
        t = T[i]
        if t==pt:
            continue

        for j in range(len(t)):
            if pt[j]+t[j]>pt[j+1]+t[j]:
                T[i][j] = pt[j]+t[j]
            else:
                T[i][j] = pt[j+1]+t[j]

        pt = t

    print(T[0][0])