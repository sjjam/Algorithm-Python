# 숨바꼭질
# https://www.acmicpc.net/problem/6118

import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

INF = int(1e9)
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
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
dist = 0
num = 0
for i in range(1, n + 1):
    if dist < distance[i]:
        dist = distance[i]
        node = i
        num = 1
    elif dist == distance[i]:
        num += 1

print(node, dist, num)