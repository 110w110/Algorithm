import sys

N = int(sys.stdin.readline())
P = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
R = [1 for _ in range(N)]

i=0
for x,y in P:
    for w,z in P:
        if x<w and y<z:
            R[i] += 1
    i += 1

print(*R,sep=' ')