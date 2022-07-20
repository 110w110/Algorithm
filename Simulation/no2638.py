# import sys
#
# N,M = map(int,sys.stdin.readline().split())
# P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# v = [[0 for _ in range(M)] for _ in range(N)]
#
# direction = [(0,-1),(0,1),(-1,0),(1,0)]
# print(*P,sep='\n')
#
# def exterior(x,y):
#     if P[y][x]!=1:
#         P[y][x]=2
#     if x>0 and x<M-1:
#         #좌우
#         if y>0 and y<N-1:
#             #상하좌우
#             for dx,dy in direction
#         elif y>0:
#             #하좌우
#         else:
#             #상좌우
#     elif x>0:
#         #우
#         if y>0 and y<N-1:
#             #상하우
#         elif y>0:
#             #하우
#         else:
#             #상우
#     else:
#         #좌
#         if y>0 and y<N-1:
#             #상하좌
#         elif y>0:
#             #하좌
#         else:
#             #상좌
#
