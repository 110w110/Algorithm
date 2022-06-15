import sys

n = int(sys.stdin.readline())
S = [int(sys.stdin.readline()) for _ in range(n)]
S.insert(0,0)
S.insert(0,0)
S.insert(0,0)
score = S[-1]
# print("score:",score)

i = n-1+3

while i>3:
    if S[i-1]+S[i-3] >= S[i-2]+S[i-3]:
        score += S[i-1]
        score += S[i-3]
        i -= 3
    else:
        score += S[i-2]
        i -= 2

    # print("score:", score)

print(score)