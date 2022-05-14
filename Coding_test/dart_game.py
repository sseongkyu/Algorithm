def solution(dartResult):
    answer = []
    num = 0
    dartResult.replace('10', 'S')
    for i in dartResult:
        if i.isnumeric():
            if num == 1:
                num = int(10)
            else:
                num += int(i)
        elif i == "*":
            if len(answer) > 1:
                answer[-2] = answer[-2]*2
                answer[-1] = answer[-1]*2
            else:
                answer[-1] = answer[-1]*2
        elif i == "#":
            answer[-1] = answer[-1]*(-1)
        elif i == "S":
            answer.append(int(num))
            num = 0
        elif i == "D":
            answer.append(int(num)**2)
            num = 0
        elif i == "T":
            answer.append(int(num)**3)
            num = 0
    return sum(answer)
