import sys

n, k = map(int,sys.stdin.readline().split())

top = 1
bottom = 1
for i in range(k):
    top *= n - i
    bottom *= i+1
print(int(top/bottom))
