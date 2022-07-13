import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
E = list(tuple(map(int,sys.stdin.readline().split())) for _ in range(m))
S, T = map(int,sys.stdin.readline().split())

# print(E)

P = [[10**9 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]
visited_count = 0

for s,t,c in E:
    P[s-1][t-1] = c

print(*P,sep='\n')

V = S-1
visited[V] = 1
visited_count += 1
cost = P[V]
path = [V+1]

print(cost)

while visited_count<n:
    m, mi = 10*9, -1
    for i in range(n):
        if i!=V and visited[i]!=1:
            if m>cost[i]:
                m = cost[i]
                mi = i
    visited[mi]=1
    visited_count+=1
    path.append(mi+1)

    for i in range(n):
        if i!=V and i!=mi:
            if cost[i]>P[mi][i]+m:
                cost[i]=P[mi][i]+m

    print('path',path)
    print('cost',cost)

    if mi==T-1:
        break

# print(visited,visited_count)
# print(*P,sep='\n')
