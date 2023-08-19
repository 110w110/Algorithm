# 33m52s solved
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def solution(p):
    if p == '':
        return p

    # u,v 분리
    a, b = 0, 0
    i = 1
    if p[0] == '(':
        a += 1
    else:
        b += 1
    while a != b:
        if p[i] == '(':
            a += 1
        else:
            b += 1
        i += 1

    u = p[:a + b]
    v = ''
    if len(u) < len(p):
        v = p[a + b:]

    # print(u, v, i)

    # u 확인
    isValid = True
    q = deque()
    for ui in u:
        if ui == '(':
            q.append(ui)
        elif q == deque():
            isValid = False
        else:
            q.pop()
    #     print(q)
    # print(isValid, u, v)

    # u가 올바르면
    if isValid:
        return u + solution(v)
    # u가 올바르지 않으면
    else:
        r = '('
        r += solution(v)
        r += ')'
        for ri in u[1:-1]:
            r += '(' if ri == ')' else ')'
        # print(r)
        return r

    return ''
