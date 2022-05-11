from functools import reduce


def solution(arr):
    return sum(arr)/len(arr)


# 람다 함수 활용
def avg(arr):
    return reduce(lambda x, y: x + y, list) / len(list)
