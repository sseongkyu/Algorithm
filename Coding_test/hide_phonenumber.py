# 내 통과코드
def hide_num(ph_num):
    num = list(ph_num)
    for i in range(len(num[:-4])):
        num[i] = '*'
    hide_num = ''.join(num)
    return hide_num

# 다른사람 풀이


def hide_num2(ph_num):
    return '*'*(len(ph_num)-4)+ph_num[-4:]


print(hide_num2('01033334444'))
