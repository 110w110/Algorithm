import re
n = 10000

a = int(input())
result = []
i = 0
while len(result) < a :
    if re.match(r'([0-9]*)(666)([0-9]*)',str(i)):
        result.append(i)
    i += 1

print(result[-1])