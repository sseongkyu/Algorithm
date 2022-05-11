# 시간초과
def solution(x, n):
    answer = []
    for i in range(x, x*(n+1), x):
        answer.append(i)
    return answer

# 통과


def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

# 다른사람 코드


def solutions(x, n):
    return [x*i for i in range(1, n+1)]
