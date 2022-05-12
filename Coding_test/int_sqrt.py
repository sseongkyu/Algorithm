from math import sqrt, pow, trunc


def solution(n):
    x = trunc(sqrt(n))
    return pow(x+1, 2) if n == pow(x, 2) else -1

# 다른사람 코드


def solution(n):
    sqrt = n**(1/2)  # 제곱근
    if sqrt % 1 == 0:  # 정수 판별
        return (sqrt+1)**2
    return -1
