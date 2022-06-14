import sys

n = int(sys.stdin.readline())

l = []

for _ in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))

l = sorted(l,key=lambda x : (x[1],x[0]), reverse=True)

print(l)
count = 1
i = len(l)-2
t = l[i+1][0]
# while t>0:
#     # l[i][0] 시작시간 l[i][1] 끝시간
#     # 끝시간 <= 현재시간 중에서 시작시간 제일 느린것
#