import sys

n = int(sys.stdin.readline())

c=1
i=0
while True:
    if n==1:
        i += 1
        break
    if c >= n:
        break
    c = c + (6*i)
    i += 1
print(i)