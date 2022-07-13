import sys
sys.setrecursionlimit(10**9)

mem = {0:0, 1:1, 2:1, 3:2}
x = int(sys.stdin.readline())

def fib(n):
    if n in mem:
        return mem[n-1]
    else:
        mem[n-1] = fib(n-1) + fib(n-2)
        return mem[n-1]

print(fib(x+1)%1000000007)
