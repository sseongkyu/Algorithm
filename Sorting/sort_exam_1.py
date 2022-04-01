# 두개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어있고 모두 자연수이다
# 최대 K번 바꿔치기 연산을 수행할 수 있고 바꿔치기 연산은 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라 두 원소를 서로 바꾸는 것
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것
# N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성

# 해결 아이디어 : 매번 배열 A에서 가장작은원소와 배열 B에서 가장큰원소를 교체
#                배열 A를 오름차순, 배열 B를 내림차순 정렬(O(NlogN)을 보장하는 정렬 알고리즘 이용)


from audioop import reverse


n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
