# 43m20s solved
import itertools
def solution(user_id, banned_id):
    S = []
    P = list(itertools.permutations(user_id, len(banned_id)))
    for p in P:
        p = list(p)
        flag = True
        for i in range(len(p)):
            if check(p[i],banned_id[i]) == False:
                flag = False
                break
        if flag == True:
            S.append(tuple(sorted(p)))
    return len(set(S))

def check(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if user[i] != ban[i] and ban[i] != '*':
            return False
    return True