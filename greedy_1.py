# 예시문제1
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택가능
# 1. N에서 1을 뺸다
# 2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수

# 해결 아이디어 : N이 K로 나누어 질수있는 수까지는 1번을 진행하고 그 차이 횟수로 카운트 그리고 나누어지는 수에서는 2번 진행한다.
# 위에 것을 반복하고 N이 K보다 작아질 경우 1까지의 차이를 횟수로 카운트한다.

n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을때 반복문 탈출
    if n < k:
        break
    # 2번 수행
    result += 1
    n //= k

# 마지막 남은 수에 대해 1번 수행
result += (n-1)
print(result)
