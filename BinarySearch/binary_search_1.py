# 이진 탐색 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # 타겟값을 찾으면 인덱스 반환
    if array[mid] == target:
        return mid
    # 타겟값이 중간값보다 작으면 중간값 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 타겟값이 중간값보다 크면 중간값 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)


# n(원소의 개수), target(찾는값)을 입력
n, target = map(int, input().split())
# 전체 원소 입력
array = list(map(int, input().split()))

# 이진 탐색 수행 결과출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)
