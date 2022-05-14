def solution(dartResult):
    answer = []
    num = 0
    dartResult.replace('10', 'S')
    for i in dartResult:
        if i.isnumeric():
            if num == 1:
                num = 10
                print(num)
            else:
                num += int(i)
                print(num)
        elif i == "*":
            if len(answer) > 1:
                answer[-2] = answer[-2]*2
                answer[-1] = answer[-1]*2
                print(answer)
            else:
                answer[-1] = answer[-1]*2
                print(answer)
        elif i == "#":
            answer[-1] = answer[-1]*(-1)
            print(answer)
        elif i == "S":
            answer.append(int(num))
            num = 0
            print(answer)

        elif i == "D":
            answer.append(int(num)**2)
            num = 0
            print(answer)

        elif i == "T":
            answer.append(int(num)**3)
            num = 0
            print(answer)

    return sum(answer)


a = solution('1D2S#10S')
print(a)
