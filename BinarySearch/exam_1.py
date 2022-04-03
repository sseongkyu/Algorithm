# <문제> 정렬된 배열에서 특정 수의 개수 구하기

# N개의 원소를 포함하고 있는 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면
# 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다

# 해결 아이디어 : 표준라이브러리인 bisect_left와 bisect_right를 활용해 count_by_range함수를 만들어 해결

from bisect import bisect_left, bisect_right

# left_value와 right_value 사이의 개수를 값으로 반환하는 함수


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


# n(데이터의 개수), x(찾는값), array 입력
n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x,x]범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는 경우
if count == 0:
    print(-1)
# 값이 존재하는 경우
else:
    print(count)
