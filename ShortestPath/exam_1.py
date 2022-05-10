# <문제> 전보
# N개의 도시가 있다 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 메시지를 전송가능
# X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어야 함
# X, Y는 서로 연결되어있어야 메시지를 보낼 수 있다.
# 어느날 C라는 도시에서 응급상황이 발생, 최대한 많은 도시로 메시지를 보내고자 할 때
# 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나간다. 도시 번호와 통로가 설치되어 있는 정보가 주어졌을 때
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수와 걸리는 시간을 계산하는 프로그램


# 해결 아이디어 : 시간 제한 조건으로 인해 우선순위 큐인 Heap을 이용한 알고리즘 사용하여 C도시에서 다른 모든 도시에게 보내는데 걸리는 최소한의 시간을 구한다
import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리를 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 노드 개수, 간선 개수, 시작 노드 입력
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

# dijkstra algorithm
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1 을 출력
print(count-1, max_distance)
