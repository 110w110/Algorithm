import sys

n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int,sys.stdin.readline().split()))

r = []
# print(a)
# print(b)
a.sort()

# print(a)
# print(b)
for x in b:
    k = 0
    count = 0
    while a[k]<x:
        # print(a[k],k)
        k += 1
        if len(a)==k+1:
            break
    while a[k]==x:
        # print("::",a[k],k)
        k += 1
        count += 1
        if len(a)==k:
            break
    r.append(count)
#
for y in r:
    print(y,end=" ")
# print(r)