# 내 코드
def solution(nums):
    set_num = len(set(nums))
    if set_num >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = set_num

    return answer

# 다른사람 코드


def solution(nums):
    min(len(set(nums)), len(nums)/2)
