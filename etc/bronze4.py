import sys

n = int(input())
score = list(map(int,sys.stdin.readline().split()))

max_score = max(score)

sum = 0
for _ in range(n):
    sum += score[_]/max_score*100

print(sum/n)