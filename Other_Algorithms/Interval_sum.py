# 구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 게산하는 문제

# 접두사 합(Prefix Sum): 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것

n = 5
data = [10, 20, 30, 40, 50]
P_list = [0]
pre_sum = 0

# 접두사 합(Prefix Sum) 계산
for i in data:
    pre_sum += i
    P_list.append(pre_sum)

print(P_list)

# 구간 합 계산
left = 3
right = 4
print(P_list[right] - P_list[left-1])
