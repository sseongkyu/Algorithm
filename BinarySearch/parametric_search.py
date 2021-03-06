'''
파라메트릭 서치 : 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
        예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진탐색을 이용하여 해결가능
'''

# <문제>떡볶이 떡 만들기
# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단. 높이가 H보다 긴 떡은 H 윗부분이 잘리고 낮은 떡은 잘리지 않는다
# ex) 19,14,10,17cm 인 떡을 15cm로 자르면 떡의 높이는 15,14,10,15cm가 되고 잘린 떡의 높이는 4,0,0,2cm 이다
# 손님은 총 6cm 길이의 떡을 가져간다.
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
# 떡의 개수 n과 요청한 떡의 길이 m을 입력, 개별 떡의 높이 입력

# 해결 아이디어 : 적절한 높이를 찾을 때까지 이진탐색을 수행하여 높이 H를 반복하여 조정
# 조건의 만족여부에 따라 탐색범위를 좁혀서 해결
# Tip 탐색범위가 클 경우 이진탐색을 떠올리기

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += x-mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
