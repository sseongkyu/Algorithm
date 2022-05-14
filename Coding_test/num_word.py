# 내 코드
def solution(s):
    # 굳이 필요가 없었다....
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    word_list = ['zero', 'one', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):  # 반복은 의미있는 만큼 반복(혹 word리스트가 12개면 세는게 아니라 개수만큼 반복하려면 len함수 사용)
        s = s.replace(word_list[i], int_list[i])
    return int(s)

# 다른사람 코드


def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    return int(s)
