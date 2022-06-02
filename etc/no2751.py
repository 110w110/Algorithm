import sys

n = int(sys.stdin.readline().strip())
list = [int(sys.stdin.readline().strip()) for _ in range(n)]

list.sort()
# print(list)

for i in range(len(list)):
    print(list[i])