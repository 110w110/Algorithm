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
            return False
        if S[y][i]==k and x!=i:
            return False

    for i in range(yb,yb+4):
        for j in range(xb,xb+4):
            if S[i][j]==k and i!=y and j!=x:
                return False

    return True

findBlank()
print(Q)
