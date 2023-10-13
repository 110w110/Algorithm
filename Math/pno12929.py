def solution(s):
    left = 0
    right = 0
    for ss in s:
        if ss == '(':
            left += 1
        elif ss == ')':
            right += 1
        if left < right:
            return False
    if left != right:
        return False
    return True