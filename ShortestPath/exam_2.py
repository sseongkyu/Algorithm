# <문제> 미래 도시
# 미래 도시에는 1~N번까지의 회사가 있는데 특정회사끼리 서로 도로로 연결되어 있다.
# 방문 판매원A는 현재 1번회사에 위치, X번 회사에 방문해 물건을 판매하고자한다.
# 연결된 회사는 양방향으로 이동가능, 도로로 연결된 회사는 1만큼의 시간으로 이동가능
# 또한 A씨는 소개팅에도 참석하고자 한다. 상대는 K번 회사에 존재
# X번 회사에 가기전 k번회사에 찾아가 커피를 마시고 X번 회사에 방문할 예정(1번회사->K번회사->X번회사)
# 방문 판매원이 회사 사이를 이동하게 되는 최소시간을 계산하는 프로그램 작성

# 해결 아이디어 : 전형적인 최단거리 알고리즘 문제, N크기가 최대 100이므로 플로이드 워셜 알고리즘 사용해 해결
#                플로이드 워셜 알고리즘 수행한 뒤 (1번 노드에서 X까지의 최단거리+X에서 K까지의 최단거리)를 계산 출력

# infinity value
INF = int(1e9)

# Input node, edge
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# The cost of diagonal element is reset to 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Input edge infomation (repeat the input m times)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k company number
x, k = map(int, input().split())

# perform floyd washall algorithm
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# shortest distance calculation(1->k + k->x)
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
