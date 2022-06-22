# import sys
# from collections import deque
#
# M, N = map(int,sys.stdin.readline().split())
# deq = deque([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
# q = deque()
#
# days = 0
#
# count = 0
# for i in range(N):
#     for j in range(M):
#         if deq[i][j] == 1:
#             q.append((j, i))
#         elif deq[i][j] == 0:
#             count += 1
#
# def ext(x,y):
#     if x!=0:
#         q.append((x-1,y))
#     if x!=M-1:
#         q.append((x+1,y))
#     if y!=0:
#         q.append((x,y-1))
#     if y!=N-1:
#         q.append((x,y+1))
#     print(q)
#
# # print(q)
# while True:
#     isChanged = False
#     if count == 0:
#         break
#
#     while q:
#         w = q.popleft()
#         x = w[0]
#         y = w[1]
#         if x!=0 and deq[y][x-1]==0:
#             isChanged = True
#             deq[y][x-1] = 1
#             ext(x-1,y)
#         if x!=M-1 and deq[y][x+1]==0:
#             isChanged = True
#             deq[y][x+1] = 1
#             ext(x+1,y)
#         if y!=0 and deq[y-1][x]==0:
#             isChanged = True
#             deq[y-1][x] = 1
#             ext(x,y-1)
#         if y!=N-1 and deq[y+1][x]==0:
#             isChanged = True
#             deq[y+1][x] = 1
#             ext(x,y+1)
#
#     print(q)
#
#     if isChanged==False:
#         days = -1
#         break
#
#     days += 1
#
# print(days)

# import sys
# from collections import deque
#
# M, N = map(int,sys.stdin.readline().split())
# T = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# q = deque()
#
# direction = [(0,-1),(0,1),(-1,0),(1,0)]
# days = 0
# count = 0
#
# for i in range(N):
#     for j in range(M):
#         if T[i][j] == 1:
#             q.append((j,i))
#         elif T[i][j] == 0:
#             count += 1
#
# if count == 0:
#     days = -1
# else:
#     while q:
#         isChanged = False
#         x,y = q.popleft()
#         while q:
#             tmpx, tmpy = q.popleft()
#             if x != tmpx or y != tmpy:
#                 q.appendleft((tmpx,tmpy))
#                 break
#         # print(x,y)
#         for d in direction:
#             dx = x + d[0]
#             dy = y + d[1]
#             if dx >= 0 and dx < M and dy >= 0 and dy < N:
#                 print(dx,dy)
#                 if T[dy][dx]==0:
#                     T[dy][dx]=1
#                     isChanged = True
#                     for dd in direction:
#                         ddx = dx + dd[0]
#                         ddy = dy + dd[1]
#                         # print(dx,dy,'->',ddx,ddy)
#                         if ddx >= 0 and ddx < M and ddy >= 0 and ddy < N:
#                             if (ddx != dx or ddy != dy) and (ddx != x or ddy != y):
#                                 q.append((ddx,ddy))
#             # print(dx,dy)
#         days += 1
#         print(q)
#         print(*T,sep="\n")
#         if isChanged==False:
#             break
# print(days)