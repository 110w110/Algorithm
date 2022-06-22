import sys

N, K = map(int, sys.stdin.readline().split())
global count
count = 0

def f(x):
    global count
    if str(type(x))!="<class 'float'>":
        a = min(abs(x/2-N),abs(x-1-N),abs(x+1-N))
        b = min(abs((x-1)*2-N),abs((x+1)*2-N))
        print("1",a,b)
        if a<=b:
            count += 1
            if a == 0:
                return count
            else:
                f(a)
        else:
            count += 2
            if b == 0:
                return count
            else:
                f(b)
    else:
        a = min(abs(x-0.5-N),abs(x+0.5-N))
        print("2",a)
        if a == 0:
            return count
        else:
            f(a)

print(f(K))