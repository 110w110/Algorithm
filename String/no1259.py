import sys
list = []
list.append(sys.stdin.readline().strip())

while True:
    list.append(sys.stdin.readline().strip())
    if list[-1] == '0':
        break

for x in list:
    if x == '0':
        break
    while len(x)>1:
        if x[0]!=x[-1]:
            break
        x = x[1:-1]
    if len(x)<=1:
        print('yes')
    else:
        print('no')