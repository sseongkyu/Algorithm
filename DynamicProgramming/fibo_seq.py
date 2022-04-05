def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


print(fibo(4))

# 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게되고
# 중복되는 부분이 발생하는 문제가 있다
