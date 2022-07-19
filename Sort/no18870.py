import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

t = list(set(l))
t.sort()
d = {n: i for i,n in enumerate(t)}

for i in range(len(l)):
    l[i] = d[l[i]]
print(*l)