INF = int(1e9)  # infinity value

# input node, edge
n = int(input())
m = int(input())
# make 2Dimension list, reset to infinity
graph = [[INF] * (n+1) for _ in range(n+1)]

# The Cost of the diagonal element is reset to 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Input the information of each edge and initializes
for _ in range(m):
    # Cost of going from A to B is C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# perform floyd warshall algorithm according to the recurrence relation
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# result
for a in range(1, n+1):
    for b in range(1, n+1):
        # value == INF
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # valid value
        else:
            print(graph[a][b], end=' ')
    print()
