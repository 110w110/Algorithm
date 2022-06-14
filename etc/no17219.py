import sys

n, m = map(int, sys.stdin.readline().split())

l = [list(sys.stdin.readline().split()) for _ in range(n)]
l = sorted(l,key=lambda x:x[0])
s = [sys.stdin.readline().strip() for _ in range(m)]
# s.sort()

# print(l)
# print(s)

# i = 0
for x in s:
    i = 0
    while l[i][0]!=x:
        i += 1
    # print(l[i])
    print(l[i][1])
    # del l[i]
    # print(l)
