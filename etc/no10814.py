import sys

n = int(sys.stdin.readline().strip())
list = [tuple(sys.stdin.readline().split()) for _ in range(n)]

list = sorted(list,key = lambda x : (int(x[0])))
# print(list)

for x in list:
    print(x[0],x[1])