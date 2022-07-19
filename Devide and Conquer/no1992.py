import sys

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]

print(*l,sep='\n')

