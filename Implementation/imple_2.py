# 정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

# 해결 아이디어 : 하루 86400초이므로 모든 경우의 수를 하나씩 세서 푸는 문제
# 완전 탐색(Brute Forcing) 문제 유형

n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
