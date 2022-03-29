# N x M 크기의 직사각형 미로 문제
# 초기 위치 (1,1) 출구는 (N,M)이다 한 번에 한 칸 이동가능
# 괴물이 있는 위치 0, 없는 부분은 1로 표시, 움직여야하는 최소 칸의 개수를 구하는 프로그램
# 칸을 셀 때 시작 칸과 마지막 칸을 모두 포함해서 계산

# 해결 아이디어 : BFS를 활용하여 시작 지점에서 인접한 노드부터 차례로 탐색하여 모든 노드를 탐색
# (1,1)지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결가능
# step1. (1,1)위치에서 시작
# step2. 상하좌우 탐색을 진행하여 바로 옆 노드인 (1,2)위치의 노드를 방문하여 새로 방문하는 노드의 값을 2로 변경
# step3. 반복적으로 BFS를 수행하면 최단 경로의 값들이 1씩 증가하는 형태로 변경
from collections import deque


def bfs(x, y):
    # 큐(queue)를 구현하기 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 나가면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


# n,m 크기 입력
n, m = map(int, input().split())

# 2차원 리스트 맵정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
