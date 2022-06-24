import sys
# print(4*4+9+6*2*2*3)
N, M = map(int,sys.stdin.readline().split())
l = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def squareSum(x,y):
    result = 0
    for i in range(5):
        result += l[y][x] + l[y][x+1] + l[y][x+2] + l[y][x+3]
    return result

# print(squareSum(0,0))

def findLargestSquare(n,m):
    x,y = 0,0
    max = 0
    for i in range(n-3):
        for j in range(m-3):
            # print(j,i)
            t = squareSum(j, i)
            if t > max:
                x,y = j,i
                max = t
    return x,y

def findSumofShape(x,y):
    M = 0
    # I shape 4*2
    for i in range(4):
        tmp = l[y+i][x] + l[y+i][x+1] + l[y+i][x+2] + l[y+i][x+3]
        if tmp > M:
            M = tmp
    for i in range(4):
        tmp = l[y+0][x+i] + l[y+1][x+i] + l[y+2][x+i] + l[y+3][x+i]
        if tmp > M:
            M = tmp

    # square 3*3
    for i in range(3):
        for j in range(3):
            tmp = l[y+i][x+j] + l[y+i][x+j+1] + l[y+i+1][x+j] + l[y+i+1][x+j+1]
            if tmp > M:
                M = tmp

    # L shape 6*2*2
    for i in range(2):
        for j in range(3):
            tmp = []
            # 세로
            tmp.append(l[y + i][x + j] + l[y + i + 1][x + j] + l[y + i + 2][x + j] + l[y + i + 2][x + j + 1])
            tmp.append(l[y + i][x + j] + l[y + i + 1][x + j] + l[y + i + 2][x + j] + l[y + i][x + j + 1])
            tmp.append(l[y + i][x + j + 1] + l[y + i + 1][x + j + 1] + l[y + i + 2][x + j + 1] + l[y + i][x + j])
            tmp.append(l[y + i][x + j + 1] + l[y + i + 1][x + j + 1] + l[y + i + 2][x + j + 1] + l[y + i][x + j])

            tmp.append(l[y + i][x + j] + l[y + i + 1][x + j] + l[y + i + 1][x + j + 1] + l[y + i + 2][x + j + 1])
            tmp.append(l[y + i][x + j + 1] + l[y + i + 1][x + j] + l[y + i + 1][x + j + 1] + l[y + i + 2][x + j])

            tmp.append(l[y + i][x + j] + l[y + i + 1][x + j] + l[y + i + 2][x + j ] + l[y + i + 1][x + j + 1])
            tmp.append(l[y + i][x + j + 1] + l[y + i + 1][x + j + 1] + l[y + i + 2][x + j + 1] + l[y + i + 1][x + j])

            m = max(tmp)
            if m > M:
                M = m

    for i in range(3):
        for j in range(2):
            tmp = []
            # 가로
            # print(x,y,j,i)
            tmp.append(l[y + i][x + j] + l[y + i][x + j + 1] + l[y + i][x + j + 2] + l[y + i + 1][x + j + 2])
            tmp.append(l[y + i][x + j] + l[y + i][x + j + 1] + l[y + i][x + j + 2] + l[y + i + 1][x + j])
            tmp.append(l[y + i + 1][x + j] + l[y + i + 1][x + j + 1] + l[y + i + 1][x + j + 2] + l[y + i][x + j + 2])
            tmp.append(l[y + i + 1][x + j] + l[y + i + 1][x + j + 1] + l[y + i + 1][x + j + 2] + l[y + i][x + j])

            tmp.append(l[y + i][x + j] + l[y + i][x + j + 1] + l[y + i + 1][x + j + 1] + l[y + i + 1][x + j + 2])
            tmp.append(l[y + i][x + j + 2] + l[y + i][x + j + 1] + l[y + i + 1][x + j + 1] + l[y + i + 1][x + j])

            tmp.append(l[y + i][x + j] + l[y + i][x + j + 1] + l[y + i][x + j + 2] + l[y + i + 1][x + j + 1])
            tmp.append(l[y + i + 1][x + j] + l[y + i + 1][x + j + 1] + l[y + i + 1][x + j + 2] + l[y + i][x + j + 1])

            m = max(tmp)
            if m > M:
                M = m

    # Z shape 6*2*2

    # T shape 6*2*2
    return M

x,y = findLargestSquare(N,M)
# print(x,y)
print(findSumofShape(x,y))