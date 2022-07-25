import sys

R, C, M = map(int,sys.stdin.readline().split())
Shark = {i:list(map(int,sys.stdin.readline().split())) for i in range(M)}
count = 0
Grid = [[[] for _ in range(C)] for _ in range(R)]
direction = {1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}

for shark in Shark:
    r,c,s,d,z = Shark[shark]
    Grid[r-1][c-1].append(shark)
    # print(r,c)
    # Grid[r-1][c-1].append((s,d,z))

# print(*Grid,sep='\n')
# print(Shark)

# 1. fisher move
for fisher in range(C):
    # print('fisher in column',fisher+1)
    # print(Grid[0][fisher])

    # 2. fishing
    for row in range(R):
        if Grid[row][fisher]!=[]:
            # print('row, fisher',row,fisher)
            count += Shark[Grid[row][fisher][0]][4]
            Shark[Grid[row][fisher][0]] = None
            Grid[row][fisher]=[]
            break

    # 3. shark move
    for shark in Shark:
        if Shark[shark]==None:
            continue
        r,c,s,d,z = Shark[shark]
        Grid[r-1][c-1] = []
        ns = s
        if d==1 or d==2:
            ns %= (R-1)*2
        else:
            ns %= (C-1)*2

        if ns==0:
            if nr==1 and d==1:
                d = 2
            elif nr==R and d==2:
                d = 1
            elif nc==1 and d==4:
                d = 3
            elif nc==C and d==3:
                d = 4
            Grid[r - 1][c - 1].append(shark)
            Shark[shark] = [r,c,s,d,z]
        else:
            nr, nc = r, c
            while ns>0:
                if nr==1 and d==1:
                    d = 2
                elif nr==R and d==2:
                    d = 1
                elif nc==1 and d==4:
                    d = 3
                elif nc==C and d==3:
                    d = 4

                nr += direction[d][0]
                nc += direction[d][1]
                ns -= 1

            # print(shark,r,c,nr,nc)
            Grid[nr-1][nc-1].append(shark)
            Shark[shark] = [nr,nc,s,d,z]

    for r in range(R):
        for c in range(C):
            if len(Grid[r][c])>1:
                smax = 0
                s = -1
                for i in Grid[r][c]:
                    if Shark[i][4]>smax:
                        smax = Shark[i][4]
                        s = i
                for i in Grid[r][c]:
                    if i!=s:
                        Shark[i]=None

                Grid[r][c]=[s]


    # print()
    # print(*Grid, sep='\n')


# print(*Grid,sep='\n')
# print(Shark)
print(count)