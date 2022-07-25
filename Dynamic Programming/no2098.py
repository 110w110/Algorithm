import sys

N = int(sys.stdin.readline())

W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

print(*W,sep='\n')

R = [{} for _ in range(N)]

# R[0][(1,2)] = 3

# print(R[0])
def TSP(i,v):
    if v in R[i]:
        return R[i][v]
    print(tuple(list(v)+[3]))

TSP(0,(2))
# print(TSP(0,(1,2)))