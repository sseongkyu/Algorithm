def solution(numbers, hand):
    # 키패드 위치를 배열로 지정
    keypad_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                   4: [1, 0], 5: [1, 1], 6: [1, 2],
                   7: [2, 0], 8: [2, 1], 9: [2, 2],
                   '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    # 왼손,오른손 초기위치 및 현재위치 저장
    l_h = '*'
    r_h = '#'
    answer = ''
    for i in numbers:
        # 1,4,7인 경우 무조건 왼손
        if i in (1, 4, 7):
            answer += 'L'
            l_h = i
        # 3,6,9인 경우 무조건 오른손
        elif i in (3, 6, 9):
            answer += 'R'
            r_h = i
        # 2,5,8,0인 경우 현재 왼손오른손 위치에서 누를 위치가 가까운 손으로 터치, 같으면 주손으로 터치
        else:
            # 현재 위치
            l_loc = keypad_dict[l_h]
            r_loc = keypad_dict[r_h]

            # 누를 키패드와 현재 손의 거리
            l_dis = abs(keypad_dict[i][0]-l_loc[0]) + \
                abs(keypad_dict[i][1]-l_loc[1])
            r_dis = abs(keypad_dict[i][0]-r_loc[0]) + \
                abs(keypad_dict[i][1]-r_loc[1])

            # 2,5,8,0 인 경우 왼손오른손 거리 계산 후 터치
            if l_dis < r_dis:
                answer += 'L'
                l_h = i
            elif r_dis < l_dis:
                answer += 'R'
                r_h = i
            # 거리가 같은 경우 주손으로 터치
            else:
                if hand == 'right':
                    answer += 'R'
                    r_h = i
                else:
                    answer += 'L'
                    l_h = i

    return answer
