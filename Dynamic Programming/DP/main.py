#백준 1520번 내리막길
#70%대에서 틀렸습니다 나옴
def find(sx, sy, dx, dy):
    if (sx,sy,dx,dy) in mem:
        return mem[(sx,sy,dx,dy)]

    if (abs(sx-dx) == 0 and abs(sy-dy) == 1) or (abs(sy-dy) == 0 and abs(sx-dx) == 1):  #s와 d의 거리가 상하좌우 한칸 차이일때
        if arr[sy][sx] > arr[dy][dx]:          #s의 높이가 d보다 높으면 경로는 1개로 반환
            return 1
        else:                                   #s의 높이가 더 높지 않으면 경로는 없음
            return 0
    elif (sx - dx == 0 and sy - dy == 0):
        return 1
    else:                                       #거리가 한칸보다 멀 때 상하좌우 한칸을 경유해서 가는 길을 모두 계산
        up = 0
        down = 0
        left = 0
        right = 0

        if sy != 0: # up 가능
            if arr[sy][sx] > arr[sy-1][sx] and arr[sy-1][sx] > arr[dy][dx]:
                up = 1 * find(sx, sy-1, dx, dy)
        if sy != m-1: # down 가능
            if arr[sy][sx] > arr[sy+1][sx] and arr[sy+1][sx] > arr[dy][dx]:
                down = 1 * find(sx, sy+1, dx, dy)
        if sx != 0: #left 가능
            if arr[sy][sx] > arr[sy][sx-1] and arr[sy][sx-1] > arr[dy][dx]:
                left = 1 * find(sx-1, sy, dx, dy)
        if sx != n-1: #right 가능
            if arr[sy][sx] > arr[sy][sx+1] and arr[sy][sx+1] > arr[dy][dx]:
                right = 1 * find(sx+1, sy, dx, dy)

        mem[(sx,sy,dx,dy)] = up + down + left + right
        return up + down + left + right         #모든 경로의 경우의 수를 합해서 반환

mem = {}
global m, n
inp = input()
inp_s = inp.split()
m = int(inp_s[0])   #세로
n = int(inp_s[1])   #가로
global arr
arr = []
for i in range(m):  #세로갯수만큼 반복해서 입력받음
    tmp = input()
    arr.append(list(map(int,tmp.split())))

print(find(0, 0, n-1, m-1)) #(0,0)에서 (n-1,m-1)로 가는 경로 출력