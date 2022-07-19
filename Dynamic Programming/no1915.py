# 가장 큰 정사각형 :: 1915
# 문제
# n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.
#
# 0	1	0	0
# 0	1	1	1
# 1	1	1	0
# 0	0	1	0
# 위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.
#
# 입력
# 첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.
#
# 출력
# 첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.
#
# 4 4
# 0100
# 0111
# 1110
# 0010
#
# 4 6? 6 4?
# 4 6
# 010011
# 011110
# 111111
# 001111
#
# 4

max = 0
P = []
n, m = map(int,input().split())

for _ in range(n):
    row = []
    tmp = input()
    for _ in range(m):
        row.append(int(tmp[0]))
        tmp=tmp[1:]
    P.append(row)

for t in P:
    if 1 in t:
        max = 1
else:
    for j in range(1,n):
        for i in range(1,m):
            if P[j][i]!=0:
                L = []
                L.append(P[j][i-1])
                L.append(P[j-1][i])
                L.append(P[j-1][i-1])
                L.sort()
                if len(L)!=0:
                    P[j][i]=L[0]+1
                    if P[j][i] > max:
                        max = P[j][i]

print(max*max)