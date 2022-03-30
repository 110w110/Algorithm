def task(O,P,n,m):
    # print(A[n] + str(n) + ' ' + B[m] + str(m))
    if A[n] == B[m]:
        panalty = 0
    else:
        panalty = 1
    gap = 2
    O[m][n]=min(O[m+1][n+1]+panalty,O[m+1][n]+gap,O[m][n+1]+gap)
    if O[m][n]==O[m+1][n+1]+panalty:
        if panalty==0:
            P[m][n]=0
        else:
            P[m][n]=1
    elif O[m][n]==O[m+1][n]+gap:
        P[m][n]=2
    else:
        P[m][n]=3

def initO(O, n, m):
    for i in range(n):
        O[m-1][i] = (n - i - 1) * 2
    for j in range(m):
        O[j][n-1] = (m - j - 1) * 2
    return O

def path(P,n,m):
    i=0
    j=0
    result=0
    while i!=n or j!=m:
        if P[j][i] == 0:
            i=i+1
            j=j+1
            # print(A[i-1]+' '+B[j-1])
            result=result+1
        elif P[j][i] == 1:
            i=i+1
            j=j+1
            # print(A[i-1]+' '+B[j-1])
        elif P[j][i] == 2:
            j=j+1
            # print('- '+B[j-1])
        else:
            i=i+1
            # print(A[i-1]+' -')
    if P[m][n]==0:
        result=result+1
    return result

A = input()
B = input()
S = ""

n = len(A)
m = len(B)

O = [[0 for x in range(n+1)] for y in range(m+1)]
P = [[0 for x in range(n)] for y in range(m)]

O = initO(O,n+1,m+1)
# task(O,P,n,m)

for i in range(m):
    for j in range(n):
        # print(str(n-j-1) + ' ' + str(m-i-1))
        task(O,P,n-j-1,m-i-1)

# print(O)
for i in range(m+1):
    print(O[i])
for i in range(m):
    print(P[i])

# print(S)
print(path(P,n-1,m-1))