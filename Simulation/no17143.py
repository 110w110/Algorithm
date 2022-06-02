# 문제
# 낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다.
# 격자판의 각 칸은 (r, c)로 나타낼 수 있다.
# r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다.
# 칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.
#
# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
#
# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
# 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다.
# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
#
# 왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다.
# 상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력이다.
# 왼쪽 위에 상어를 구분하기 위해 문자를 적었다.
#
# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
# 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
#
# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.
#
# 입력
# 첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
#
# 둘째 줄부터 M개의 줄에 상어의 정보가 주어진다.
# 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다.
# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
#
# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
#
# 출력
# 낚시왕이 잡은 상어 크기의 합을 출력한다.
#
# 예제 입력 1  복사
# 4 6 8
# 4 1 3 3 8
# 1 3 5 2 9
# 2 4 8 4 1
# 4 5 0 1 4
# 3 3 1 2 7
# 1 5 8 4 3
# 3 6 2 1 2
# 2 2 2 3 5
# 예제 출력 1  복사
# 22

# import sys
# sum = 0
# R, C, M = map(int,sys.stdin.readline().split())
# S = []
# # print(R,C,M)
# for m in range(M):
#     r, c, s, d, z = map(int,sys.stdin.readline().split())
#     S.append([r,c,s,d,z])
#
# T = [[[[0,0,0,0,0]] for _ in range(C)] for _ in range(R)]
# # print(T)
#
# for t in S:
#     T[t[0]-1][t[1]-1][0] = t
#
# for tmp in T:
#     print(tmp)
#
# for P in range(C):
#     for check1 in T:
#         for check2 in check1:
#             if len(check2)!=1:
#                 # print(check2)
#                 check2 = max(check2,key=lambda x:x[4])
#                 # print(check2)
#     # 상어잡기 i 순환
#     i = 0
#     while T[i][P][0][4]==0 and i<R-1 : i+=1
#     print(i,P)
#     if T[i][P][0][4]!=0:
#         sum += T[i][P][0][4]
#         print(T[i][P][0],"낚시 성공")
#         T[i][P][0] = [0,0,0,0,0]
#     # 상어이동
#     for j in S:
#         r = j[0]
#         c = j[1]
#         s = j[2]
#         d = j[3]
#         z = j[4]
#         # # 잡아먹힌 상어는 넘어감
#         # if z == 0: continue
#         if d < 3 :
#             s = s % (R*2)
#             if s >= R : move = ((d * 2) - 3) * (s-R)
#             else : move = ((d * 2) - 3) * (-1) * (s)
#             if T[r-1][c-1][0][4] > T[r-1+move][c-1][0][4]:
#                 T[r-1+move][c-1][0] = T[r-1][c-1][0]
#             T[r-1][c-1][0] = [0,0,0,0,0]
#             print(r-1, c-1, " -> ",r-1+move,c-1)
#         else :
#             s = s % (C*2)
#             if s >= C : move = (((d - 2) * 2) - 3) * (-1) * (s-R)
#             else : move = (((d - 2) * 2) - 3) * (s)
#             if T[r-1][c-1][0][4] > T[r-1][c-1+move][0][4]:
#                 T[r-1][c-1+move][0] = T[r-1][c-1][0]
#             T[r-1][c-1][0] = [0,0,0,0,0]
#             print(r-1, c-1, " -> ",r-1,c-1+move)
#     print("#"*30)
#     for tmp in T:
#         print(tmp)
#
# print(sum)


import sys
sum = 0
R, C, M = map(int,sys.stdin.readline().split())
S = []
# print(R,C,M)
for m in range(M):
    r, c, s, d, z = map(int,sys.stdin.readline().split())
    S.append([r,c,s,d,z])
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.

T = [[(0,0,0) for _ in range(C)] for _ in range(R)]

for t in S:
    T[t[0]-1][t[1]-1] = (t[2],t[3],t[4])

for tmp in T:
    print(tmp)

def move(y,x):
    print(T[y][x])
    isHorizontal = True if T[y][x][1] > 2 else False
    s = T[y][x][0]
    d = -((T[y][x][1] * 2) - 3) if T[y][x][1] <= 2 else -((T[y][x][1] - 2) * 2 - 3)
    z = T[y][x][2]

    if isHorizontal:
        real_d = d if (d/(C-1))%2==1 else -d
        # real_s = s%(C-1) if (s/(C-1))%2==1 else (C-1)*2-(s%((C-1)*2))
        real_s = s%((C-1)*2) if s%((C-1)*2)==1 and s <= x else abs(x%((C-1)*2)-s%((C-1)*2))
        print(x%((C-1)*2),s%((C-1)*2))
    else:
        real_d = d if (d/(R-1))%2==1 else -d
        real_s = s%(R-1) if s%((R-1)*2)==1 and s <= y else abs(y%((R-1)*2)-s%((R-1)*2))
        print(y%((R-1)*2),s%((R-1)*2))
    # print(R,C)
    print(s,d,z)
    print(real_s,real_d,z)
    # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
    # d 처리 -> 상하 12 좌우 43 이니까
    # 상하면 (d*2)-3 좌우면 -((d-2)*2-3)로 방향 계산
    # x축 이동이면 이동거리/column 과 이동거리%column 구하고, y축이면 이동거리/row 와 이동거리%row 구함
    # 실제 이동방향은 몫이 홀수면 정방향, 짝수면 역방향
    # 나머지가 실제 이동거리

    #5      (R-1)*2로 나누고 R-(y%(R-1)*2)
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    # 0 1 2 3 2 1 0 1 2 3 2  1  0  1  2
    # 0 1 2 3 4 5 0 1 2 3 4  5  0  1  2

    # 8
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    # 0 1 2 3 4 3 2 1 0 1 0  1  2  3  4
    # 0 1 2 3 4 5 6 7 8 9 0  1  2  3  4

move(0,2)
move(0,4)
move(1,1)