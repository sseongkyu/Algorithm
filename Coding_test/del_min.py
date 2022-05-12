def solution(arr):
    if len(arr) > 1:
        return arr.remove(min(arr))
    else:
        return [-1]
