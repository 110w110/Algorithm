import sys

m = int(sys.stdin.readline())
S = []
I = []
for _ in range(m):
    I.append(sys.stdin.readline().strip())

# print(I)
for line in I:
    if line=="all":
        S.clear()
        S = [i+1 for i in range(20)]
    elif line=="empty":
        S.clear()
    else:
        op, n = line.split()
        n = int(n)

        if op=="add":
            S.append(n)
        elif op=="remove":
            S.remove(n)
        elif op=="check":
            if n in S:
                print(1)
            else:
                print(0)
        elif op=="toggle":
            if n in S:
                S.remove(n)
            else:
                S.append(n)


# print(S)
