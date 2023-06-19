from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for t in topping:
        left.add(t)
        right[t] -= 1
        
        if right[t] == 0:
            del right[t]
        if len(left) == len(right):
            answer += 1
        
    return answer

# 1) 안됨
# set에 넣고 갯수 세서 전체 종류 수를 알아냄
# 순서대로 탐색하다가 전체 종류 수의 반만큼 도달하면 반을 넘어서기 전까지 answer에 카운트
# X -> 토핑의 위치에 따라 전체 종류 수와 관련 없음

# 2)
# 이분탐색으로 중간 잘라서 양 옆 set으로 종류 수 확인
# 같으면 양 옆으로 달라질 때까지 움직이면서 카운트
# 다르면 한쪽으로 움직이면서 같아질 때 찾아보고 뒤집히면 그냥 종료해서 0개로 카운트
# X -> 중간부터 자르면 좌우로 움직이는 방향 고려하기가 복잡해짐

# 3)
# 그냥 처음부터 쭉 가면서 set으로 개수 비교해보기
# X -> 시간초과

# 4)
# Set과 Counter를 둘다 써서 양쪽 비교하기
