# 여행가 A는 NxN크기의 정사각형 공간위에 서있다. 공간은 1 x 1 크기의 정사각형으로 나누어져있다.
# 가장 왼쪽 위 좌표(1,1) 가장 오른쪽 아래 좌표 (N,N)
# 여행가는 상,하,좌,우 이동가능 시작좌표는 항상 (1,1)
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀있다.
# L : 왼쪽으로 한칸
# R : 오른쪽으로 한칸
# U : 위로 한칸
# D : 아래로 한칸
# N x N 공간을 벗어나는 움직임은 무시  ex) (1,1)위치에서 L,U는 무시된다

# N = 5인 지도와 계획서를 사용

# 해결 아이디어 : 시물레이션의 유형, 구현이 중요한 문제

n = int(input())
x, y = 1, 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
