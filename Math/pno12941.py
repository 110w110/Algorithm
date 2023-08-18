# from itertools import permutations
# def solution(A,B):
#     answer = 1e9

#     T = [[A[i] * B[j] for i in range(len(A))] for j in range(len(B))]
#     # print(*T, sep='\n')
#     P = list(permutations([i for i in range(len(A))], len(A)))
#     # print(P)

#     for p in P:
#         s = 0
#         for i in range(len(T)):
#             s += T[i][p[i]]
#         print(s)
#         answer = min(answer, s)

#     return answer

# 17m52s solved
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer