import sys

t = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(t)]
R = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

m = max(N)
# print(m)

for i in range(9,m):
    R.append(R[i]+R[i-4])

# print(R)

for n in N:
    print(R[n-1])
