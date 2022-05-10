# <문제> 전보
# N개의 도시가 있다. 각 도시는 보내고자 하는 메시지가 있는 경우
# 다른 도시로 전보를 보내서 다른 도시로 해당메시지를 전송가능
# X->Y로 보내고자 하면, 통로가 설치되어있어야 한다.
# 어느날 C라는 도시에서 위급상황이 발생. 최대한 많은 도시로 메시지를 보내야함
# 도시 C에서 출발하여 각 도시사이에 설치된 통로를 거쳐 전송
# 각 도시의 번호, 통로가 설치된 정보가 주어졌을 때 도시 C에서 보낸 메시지를 받게되는 도시의 개수와 모두 메시지를 받는데까지 걸리는 시간을 계산하는 프로그램작성

# 해결 아이디어 : 도시사이의 최단거리 구하는 최단거리 문제로 치환
#                N과 M의 범위가 충분하므로 우선순위 큐를 활용한 다익스트라 알고리즘 구현

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# dijkjstra function declaration


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# Input node, edge, start node
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# Input information
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# perform dijkstra algorithm
dijkstra(start)

# max distance calculation
count = 0
m2ax_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)
