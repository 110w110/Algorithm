import sys
import re

t = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = re.compile(b)

prev = t
while True:
    next = re.sub(c,'',prev)
    if next==prev:
        break
    prev = next

if next == '':
    print('FRULA')
else:
    print(next)