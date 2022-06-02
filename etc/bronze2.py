a = input()
r = [0 for _ in range(26)]
max_index = -1
max_value = -1

for i in range(len(a)):
    n = ord(a[i])
    if n >= 97 and n < 123:
        n -= 97
    elif n >= 65 and n < 91:
        n -= 65
    r[n] += 1

for i in range(26):
    if r[i] > max_value:
        max_index = i
        max_value = r[i]
    elif r[i] == max_value:
        max_index = 27

if max_index == 27:
    print("?")
else:
    print(chr(max_index+65))