# 특정한 수의 범위 안에 존재하는 모든 소수를 판별하는 경우
# 에라토스테네스의 체 알고리즘
# N보다 작거나 같은 모두 소수를 찾을 때 사용
# 동작과정
# 1. 2부터 N까지의 모든 자연수 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거X)
# 4. 더 이상 반복할 수 없을 때까지 2,3번 반복

import math

n = 1000  # 1000까지의 소수 판별
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:  # i가 소수인 경우
        # i를 제외한 i의 배수 제거
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i] == True:
        print(i, end=' ')
