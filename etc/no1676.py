import sys

n = int(sys.stdin.readline())
r = 1

for i in range(n):
    r *= i+1

r = str(r)
c = 1

while True:
    if r[-c]=='0':
        c += 1
    else:
        break

print(c-1)