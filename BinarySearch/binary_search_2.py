# 이진 탐색 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은경우 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None


# n(원소의 개수)과 target(찾는값) 입력
n, target = map(int, input().split())
# 전체 원소 입력
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
