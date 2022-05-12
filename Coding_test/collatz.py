# 내 통과 코드
def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        elif num % 2 == 1:
            num = num*3+1
            count += 1
    if count > 500:
        count = -1
    return count

# 다른 사람코드
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1


# 작업을 500번 반복해서 500번안에 수행되면 for문 안에서 return값을
# 500번 이상일시에는 for문 밖에서 return값을 반환 