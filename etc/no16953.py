import sys

A, B = map(int,sys.stdin.readline().split())
count = 1
while True:
    if A==B:
        print(count)
        break
    elif A>B:
        print(-1)
        break
    # print(B)
    if B%2==0:
        B = B//2
        count +=1
    elif str(B)[-1]=='1':
        B = B//10
        count +=1
    else:
        print(-1)
        break
