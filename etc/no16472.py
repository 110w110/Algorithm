# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
# S = sys.stdin.readline().strip()
# # print(S)
#
# Q = deque()
# count = 0
# R = deque()
#
# for s in range(len(S)):
#     if S[s] not in Q:
#         Q.append(S[s])
#         R.append(count)
#         if len(Q)>N:
#             Q.popleft()
#         print('#'*10,Q,count)
#         count = 0
#     print(S[s],Q)
#
#     count += 1
#
#     if s==len(S)-1:
#         R.append(count)
#         print('end',count)
#
# print(R)
#
# # pp = ''
# # p = ''
# # for s in range(1,len(S)):
# #     count += 1
# #     if s==len(S)-1:
# #         R.append(count)
# #     if p!=S[s] and pp!=S[s]:
# #         # print(pp,p,S[s])
# #         pp = p
# #         p = S[s]
# #         R.append(count)
# #         count = 0
# # print(R)
#
# # a = R[0]
# max = 0
# for r in range(len(R)-N+1):
#     tmp = 0
#     for i in range(N):
#         tmp += R[r+i]
#     if tmp>max:
#         max = tmp
# print(max)


import sys
from collections import deque
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
D = deque()
P = deque()
print(S)

s = 0

for p in range(len(S)):
    if S[p] not in D:
        D.append(S[p])
        if len(D)>N:
            if D[-1]!=D.popleft():
                if S[p]!=S[p-1] and len(D)==N:
                    P.append(p-s)
    elif S[p]!=S[p-1]:
        D.append(S[p])
        if len(D)>N:
            D.popleft()
        s = p

    if p==len(S)-1:
        P.append(p)
    print(p,S[p],D,P,s)

print(D)
print(P)
