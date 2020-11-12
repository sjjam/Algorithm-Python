# 미래 도시

n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

def short():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i] = 1
    for i in range(n):
        now = short()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + 1
            if cost < distance[j]:
                distance[j] = cost

ans = []
dijkstra(1)
ans.append(distance[k])
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
dijkstra(k)
ans.append(distance[x])

if ans[0] == INF or ans[1] == INF:
    print(-1)
else:
    print(ans[0] + ans[1])



# 풀이

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)