import sys
global Q, S
S = [list(sys.stdin.readline().strip()) for _ in range(9)]
Q = []
print(*S,sep='\n')

def findBlank():
    global Q, S
    for i in range(9):
        for j in range(9):
            if S[i][j]=='0':
                Q.append((j,i))


def test(x,y,k):
    global S
    #x,y에 k가 들어가도 괜찮은가?
    xb=x//3*3
    yb=y//3*3

    for i in range(9):
        if S[i][x]==k and y!=i:
            print('x,y=',x,i)
            return False
        if S[y][i]==k and x!=i:
            print('x,y=',i,y)
            return False

    for i in range(yb,yb+4):
        for j in range(xb,xb+4):
            if S[i][j]==k and i!=y and j!=x:
                return False

    return True

def backtracking(ind):
    global S,Q
    if ind>=len(Q):
        return True

    x,y = Q[ind]
    # print(x,y)
    for t in range(1,10):
        print(x,y,t,test(x,y,t))
        if test(x,y,t)==False:
            continue
        else:
            S[y][x]=t
            print(*S,sep='\n')
            if backtracking(ind+1)==1:
                return True
            else:
                for i in range(ind,len(Q)+1):
                    a,b = Q[i]
                    S[b][a]=0
    return False





findBlank()
print(Q)
print(backtracking(0))