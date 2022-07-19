import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M!=0:
    L = list(map(int,sys.stdin.readline().split()))
else:
    L=[]

# +/-만 눌러서 이동하는 케이스
test1 = N - 100

K = N
x = 0
for i in range(5,-1,-1):
    c = (K%(10**(i+1)))//(10**i)
    print(c)
    if c not in L:
        x += c*(10**(i))
    else:
        for t in range(1,6):
            print(c,t)
            if c>=5:
                if c-t not in L:
                    x += (c-t)*(10**(i))
                    K = K%(10**(i))
                    tmp = 0
                    for j in range(9,5,-1):
                        if j not in L:
                            tmp = j
                            break
                    K = K%(10**(i+1))+(c-t)*(10**i)
                    for l in range(0,i):
                        K += tmp*(10**l)
                    break
                elif c+t not in L:
                    x += (c+t)*(10**(i))
                    break
            else:
                if c+t not in L:
                    x += (c+t)*(10**(i))
                    break
                elif c-t not in L:
                    x += (c-t)*(10**(i))
                    tmp = 0
                    for j in range(9,5,-1):
                        if j not in L:
                            tmp = j
                            break
                    K = K%(10**(i+1))+(c-t)*(10**i)
                    for l in range(0,i):
                        K += tmp*(10**l)
                    break

q = []
for i in range(10):
    if i not in L:
        c = len(str(N))
        # print(N-int(str(i)*c))
        # print(N-int(str(i)*(c-1)))
        q.append(abs(N-int(str(i)*c))+c)
        q.append(abs(N-int(str(i)*(c-1)))+c-1)

test3 = min(q)

test2 = abs(N - x)

print(x)
print(test1, test2+len(str(x)), test3)

print(min(test1,test2+len(str(x)),test3))