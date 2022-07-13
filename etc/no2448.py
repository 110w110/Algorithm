# import sys
# import math
# from itertools import chain,repeat
# print(3*(2**10))
#
# b = ' '
# s = '*'
# print(b*2+s+b*2)
# print(b+s+b+s+b)
# print(s*5)
#
# N = int(sys.stdin.readline())
# i = int(math.log(N//3,2))
#
# print(N,i)
# R = []
# for x in range(2**i):
#     # print(_)
#     tmp = [b*2+s+b*2,b+s+b+s+b,s*5]
#     R.append(list(chain.from_iterable(repeat(tmp,x+1))))
#     print(*R[-1])
#     # print(list(chain.from_iterable(repeat(tmp,x+1))))
#
# # print(R)
# # for i in range(len(R)):
# #     print(*R[i],sep='\n')
import sys
n = int(sys.stdin.readline())
graph = [[' '] * 2 * n for _ in range(n)]

def recursive(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        nextN = N // 2
        recursive(x, y, nextN)
        recursive(x + nextN, y - nextN, nextN)
        recursive(x + nextN, y + nextN, nextN)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))