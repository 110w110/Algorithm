# import sys
#
# N, M = map(int, sys.stdin.readline().split())
#
# l = [list(sys.stdin.readline().split()) for _ in range(N)]
# # l = sorted(l,key=lambda x:x[0])
# l.sort()
# k = [sys.stdin.readline().strip() for _ in range(M)]
# # s.sort()
#
# # print(*l,sep='\n')
# # print(s)
#
# # i = 0
# for x in k:
#     # print(x)
#     s = 0
#     t = len(l)
#     m = (t-s)//2
#     # print(m, l[m])
#     while m>=0 and m<len(l):
#         # print(m, l[m][0], x, s, m, t)
#         if l[m][0] == x:
#             print(l[m][1])
#             break
#         elif l[m][0]>x:
#             t = m
#             m = (m-s) // 2 + s
#         else :
#             s = m
#             m = (t-m-1) // 2 + s
#     # print(l[i])
#
#     # del l[i]
#     # print(l)]

import sys

N, M = map(int, sys.stdin.readline().split())

l = dict([tuple(sys.stdin.readline().split()) for _ in range(N)])
k = [sys.stdin.readline().strip() for _ in range(M)]

for x in k:
    print(l.get(x))
