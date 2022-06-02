import sys

list = [tuple(map(int,sys.stdin.readline().split()))]
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    list.append((a,b,c))
# print(list)

for x in list :
    if x[0]*x[0]+x[1]*x[1]==x[2]*x[2] or x[0]*x[0]+x[2]*x[2]==x[1]*x[1] or x[2]*x[2]+x[1]*x[1]==x[0]*x[0]:
        print("right")
    else:
        print("wrong")