# 9-1
# r1

# n, m = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x, k = map(int, input().split())

# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# ans = graph[1][k] + graph[k][x]

# if ans >= INF:
#     print('-1')
# else:
#     print(ans)



# 9-2
# r1

# import heapq

# n, m, c = map(int, input().split())
# INF = int(1e9)
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)

# for i in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
    
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue

#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(c)
# cnt = 0
# time = 0

# for i in range(1, n + 1):
#     if distance[i] != INF:
#         cnt += 1
#         time = max(time, distance[i])

# print(cnt - 1, time)



# 플로이드
# r1
# https://www.acmicpc.net/problem/11404

# n = int(input())
# m = int(input())
# INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for i in range(m):
#     a, b, c = map(int, input().split())
#     if c < graph[a][b]:
#         graph[a][b] = c

# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] == INF:
#             print(0)
#         else:
#             print(graph[i][j], end=' ')
#     print()



# 정확한 순위
# r1

# n, m = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# result = 0
# for i in range(1, n + 1):
#     cnt = 0
#     for j in range(1, n + 1):
#         if graph[i][j] != INF or graph[j][i] != INF:
#             cnt += 1
#     if cnt == n:
#         result += 1

# print(result)



# 화성 탐사
# r1 x

# import heapq

# INF = int(1e9)
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     graph = []
#     distance = [[INF] * n for _ in range(n)]

#     for i in range(n):
#         graph.append(list(map(int, input().split())))

#     x, y = 0, 0
#     q = []
#     heapq.heappush(q, (graph[x][y], x, y))
#     distance[x][y] = graph[x][y]

#     while q:
#         dist, x, y = heapq.heappop(q)
#         if distance[x][y] < dist:
#             continue
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             cost = dist + graph[nx][ny]
#             if cost < distance[nx][ny]:
#                 distance[nx][ny] = cost
#                 heapq.heappush(q, (cost, nx, ny))

#     print(distance[n - 1][n - 1])



# 숨바꼭질
# r1

import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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

dijkstra(1)

node = 0
d = 0
same = 1

for i in range(2, len(distance)):
    if distance[i] > d:
        d = distance[i]
        node = i
        same = 1
    elif d == distance[i]:
        same += 1

print(num, d, same)