n = int(input())

i = 0
if n > 100:
    i = n - 70
while True:
    sum = i + int(i/1000000)%10 + int(i/100000)%10 + int(i/10000)%10 + int(i/1000)%10 + int(i/100)%10 + int(i/10)%10 + i%10
    if sum == n:
        print(i)
        break
    if i >= n:
        print(0)
        break
    i += 1