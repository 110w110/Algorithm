def solution(x):
    k = len(list(filter(lambda x: x=='1', list(bin(x)[2:]))))
    while True:
        x += 1
        if k == len(list(filter(lambda x: x=='1', list(bin(x)[2:])))):
            return x