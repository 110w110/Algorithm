import sys

n = int(sys.stdin.readline())
l = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[0], x[1]), reverse=True)

count, t = 1, l[0][0]
for j in range(1,len(l)):
    if l[j][1]<=t:
        t = l[j][0]
        count += 1
print(count)