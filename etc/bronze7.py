import sys

x, y, w, h = map(int,sys.stdin.readline().split())

print(min(abs(w-x),abs(h-y),abs(x),abs(y)))