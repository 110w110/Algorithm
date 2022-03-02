import sys

input = int(sys.stdin.readline())
result = [0 for x in range(input + 1)]

def forOne(n) :
    result[1] = 0   # 1은 연산 0회

    for i in range(2, n+1):                     # 2에서부터 n까지 연산합의 최소를 모두 구함 (bottom to top)
        result[i] = result[i - 1] + 1           # 가장 먼저 -1의 연산에 +1회한 결과를 저장
        if i % 3 == 0:                          # 3으로 나눠질 때, 이전의 연산보다 최소이면 결과 수정
            if result[int(i / 3)] + 1 < result[i] :
                result[i] = result[int(i / 3)] + 1
        if i % 2 == 0 :                         # 2로 나눠질 때, 이전의 연산보다 최소이면 결과 수정
            if result[int(i / 2)] + 1 < result[i] :
                result[i] = result[int(i / 2)] + 1

    print(result[n])                            # n번까지의 결과를 모두 진행 후 n까지의 연산의 최소를 출력

forOne(input)


"""
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
"""