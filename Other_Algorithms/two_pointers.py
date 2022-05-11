# 리스트에 담긴 데이터에 순차적으로 접근해야할 때 시작점과 끝점 2개의 점으로 접할 데이터의 범위 표현

# 특정한 합을 가지는 부분 연속 수열 찾기

n = 5
m = 5
num_list = [1,2,3,2,5]
end = 0
count = 0
sum_num = 0

for start in range(n):
    while sum_num < m and end < n:
        sum_num += num_list[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if sum_num == m:
        count += 1
    sum_num -= num_list[start]

print(count)