a = []
max_value = -1
max_index = -1
for i in range(9):
    k = int(input())
    a.append(k)
    if k > max_value:
        max_value = k
        max_index = i + 1

print(max_value)
print(max_index)
