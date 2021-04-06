# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

import heapq

def dijkstra(start, graph, distance):
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

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in edge:
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1))
    
    dijkstra(1, graph, distance)
    maxDist = 0
    for i in range(2, n + 1):
        if distance[i] > maxDist:
            maxDist = distance[i]
            answer = 1
        elif distance[i] == maxDist:
            answer += 1
    return answer