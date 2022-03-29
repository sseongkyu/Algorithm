# N x M 크기의 얼음틀에서 구멍이 뚫린 부분 0, 칸막이가 존재하는 부분 1
# 구명이 뚫린 부분끼리는 상하좌우 연결되어있는 것으로 간주
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

# 4 x 5 틀 예시

# 해결 아이디어 : DFS/BFS 를 통해 서로 연결시켜 하나의 아이스크림으로 설정
# DFS활용
# 1. 상하좌우를 살펴 주변 지점 중 값이 0이면 아직 방문하지 않은 지점이므로 해당지점을 방문
# 2. 방문한 지점에서 다시 상하좌우를 살펴 방문을 진행하는 과정을 반복하면, 연결된 모든지점을 방문

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 얼음틀  범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았으면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


# n,m 크기의 얼음틀 입력
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대해 음료수 채우기
print(graph)
result = 0
for i in range(n):
    for j in range(m):
        print(graph)
        if dfs(i, j) == True:
            result += 1
print(result)
print(graph)
