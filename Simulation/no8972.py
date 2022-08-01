import sys
global T, k
k = False

def s():
    global T, k
    R, C = map(int,sys.stdin.readline().split())
    T = [list(sys.stdin.readline().strip()) for _ in range(R)]
    M = list(map(int,sys.stdin.readline().strip()))
    A = []
    direction = {1:(1,-1),2:(1,0),3:(1,1),4:(0,-1),5:(0,0),6:(0,1),7:(-1,-1),8:(-1,0),9:(-1,1)}
    count = 1

    # print(*T,sep='\n')
    # print(M)

    I = (0,0)
    for y in range(R):
        for x in range(C):
            if T[y][x]=='I':
                I = (y,x)
            if T[y][x]=='R':
                A.append((y,x))

    for m in M:
        # print('m',m)
        y,x = I
        nx = x + direction[m][1]
        ny = y + direction[m][0]

        # 미친 아두이노 있으면 파괴
        if T[ny][nx]=='R':
            print('kraj',count)
            k = True
            return False

        # 종수 이동
        T[y][x] = '.'
        T[ny][nx] = 'I'

        for ry,rx in A:
            nry,nrx = ry,rx
            if ny>ry:
                nry=ry+1
            elif ny<ry:
                nry=ry-1
            if nx>rx:
                nrx=rx+1
            elif nx<rx:
                nrx=rx-1
            # print(rx,ry,'->',nrx,nry)

            if T[nry][nrx]=='R':
                T[nry][nrx]='X'

                if T[ry][rx] == 'X':
                    T[ry][rx] = 'R'
                elif T[ry][rx] != 'Y':
                    T[ry][rx] = '.'
                continue
            elif T[nry][nrx] == 'Y':
                T[nry][nrx] = 'Y'

                if T[ry][rx] == 'X':
                    T[ry][rx] = 'R'
                elif T[ry][rx] != 'Y':
                    T[ry][rx] = '.'
                continue
            elif T[nry][nrx]=='X':
                T[nry][nrx]='Y'

                if T[ry][rx] == 'X':
                    T[ry][rx] = 'R'
                elif T[ry][rx] != 'Y':
                    T[ry][rx] = '.'
                continue
            elif T[nry][nrx]=='I':
                print('kraj',count)
                k = True
                return False
            else:
                # print(rx,ry,'->',nrx,nry)
                T[nry][nrx]='R'
                if T[ry][rx] == 'X':
                    T[ry][rx] = 'R'
                elif T[ry][rx] != 'Y':
                    T[ry][rx] = '.'

        A = []
        for y in range(R):
            for x in range(C):
                if T[y][x] == 'I':
                    I = (y, x)
                if T[y][x] == 'X':
                    T[y][x]='.'
                if T[y][x] == 'R':
                    A.append((y, x))
                if T[y][x] == 'Y':
                    T[y][x]='.'
        # I = (ny,nx)
        count += 1
        # print()
        #
        # for t in T:
        #     print(*t, sep='')


s()
if k==False:
    for t in T:
        print(*t,sep='')
