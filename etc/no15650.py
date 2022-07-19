import sys
from collections import deque

r = deque()

N, M = map(int,sys.stdin.readline().split())

# for i in range(N):
#     for j in range(N):
#         if (j+1,i+1) not in r:
#             r.append((i+1,j+1))
#             print(i+1,j+1)