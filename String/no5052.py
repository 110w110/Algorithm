# 문자열로 만들고 오름차순으로 정렬해서,,
# for문으로 하나씩 돌리고
# 다음 원소들 중에 같은 글자로 시작 안하면 continue
# 다음 원소 같은 글자로 시작하면
# 21 min solved

import sys
def solution(n, numbers):
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            if numbers[i] == numbers[i+1][:len(numbers[i])]:
                print('NO')
                return
    print('YES')

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [sys.stdin.readline().strip() for _ in range(n)]
    numbers.sort()
    solution(n,numbers)