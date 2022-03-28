# 왕실의 나이트
# 왕실 정원은 체스판 8 x 8 좌표 평면이다. 특정 한 칸에 나이트가 서있다
# 나이트는 L자형태로만 이동하고 정원 밖으로는 나갈 수 없다.
# 나이트의 이동 경우의수
# 1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동
# 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수 출력하는 프로그램

# 해결 아이디어 : 8가지 경로를 확인하면서 이동가능한지 확인

# 위치 입력받아서 문자와 숫자로 나누기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

# 나이트가 이동할 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 방향에 따라 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
