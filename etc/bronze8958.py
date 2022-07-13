import sys
t = int(sys.stdin.readline())
I = [sys.stdin.readline().strip() for _ in range(t)]

for line in I:
    score = 1
    result = 0
    for l in line:
        if l=='X':
            score = 1
        else:
            result += score
            score = score + 1
    print(result)
