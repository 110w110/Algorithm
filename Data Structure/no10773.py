import sys

K = int(sys.stdin.readline().strip())

list = []

for i in range(K):
    a = int(sys.stdin.readline().strip())
    if a==0:
        list.pop(-1)
    else:
        list.append(a)

print(sum(list))