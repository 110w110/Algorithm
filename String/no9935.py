import sys

T = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
Q = []
for t in T:
    if len(B)==0:
        break
    Q.append(t)
    if len(Q)<len(B):
        continue
    # print(Q,len(Q))
    while Q[-1]==B[-1]:
        if "".join(Q[-len(B):])==B:
            del Q[-len(B):]
        else:
            break
        if len(Q)<=0:
            break

if len(Q)==0:
    print('FRULA')
else:
    print(*Q,sep='')

