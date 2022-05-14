# 내 코드 (런타임 에러...)
def solution(board, moves):
    basket = []
    zero_idx = 0
    answer = 0
    board = [list(board) for board in zip(*board)]
    for i in moves:
        if board[i-1][4] == 0:
            continue
        else:
            zero_idx = max(list(
                filter(lambda x: board[i-1][x] == 0, range(len(board[i-1])))))
            basket.append(board[i-1][zero_idx+1])
            board[i-1][zero_idx+1] = 0

        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop(-1)
                basket.pop(-1)
                answer += 2
            else:
                continue
        else:
            continue
    return answer

# 개선 사항 (전치 사용 x, 해당 열의 뽑을 인형이 없으면 그만)


def solution(board, moves):
    basket = []
    zero_idx = 0
    answer = 0
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return print(answer)
