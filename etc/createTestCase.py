from random import *

print(randint(-1,1))
M=500
N=500
print(M, N)
for _ in range(N):
    for _ in range(M):
        k = randint(0,10)
        # if k < 5:
        #     print(-1,end=" ")
        # elif k < 20:
        #     print(1,end=" ")
        # else:
        #     print(0,end=" ")
        print(k,end=" ")
    print("\n",end="")

