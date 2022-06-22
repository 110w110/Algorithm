import sys

m = int(sys.stdin.readline())
S = set()
# I = []
# for _ in range(m):
#     I.append(sys.stdin.readline().strip())

# print(I)
for _ in range(m):
    line = sys.stdin.readline().strip()
    if len(line)==1:
        if line=="all":
            S = set(i+1 for i in range(21))
        elif line=="empty":
            S = set()
    else:
        op, n = line.split()
        n = int(n)

        if op=="add":
            S.add(n)
        elif op=="remove":
            S.discard(n)
        elif op=="check":
            if n in S:
                print(1)
            else:
                print(0)
        elif op=="toggle":
            if n in S:
                S.discard(n)
            else:
                S.add(n)


# print(S)
