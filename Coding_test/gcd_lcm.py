# 나의 코드
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a*b/gcd(a, b)


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

# 다른사람들 코드


def solution(n, m):
    def gcd(a, b): return b if not a % b else gcd(b, a % b)
    def lcm(a, b): return a*b/gcd(a, b)
    return [gcd(n, m), lcm(n, m)]

# 다른사람들 코드


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer
