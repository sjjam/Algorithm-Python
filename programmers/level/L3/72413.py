# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413


# 다익스트라 풀이

import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[] for _ in range(n + 1)]
    
    for i in fares:
        c, d, f = i
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start, end):
        q = []
        heapq.heappush(q, (0, start))
        distance = [INF] * (n + 1)
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
        
        return distance[end]

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer



# 플로이드 워셜 풀이

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == y:
                graph[x][y] = 0
    
    for i in fares:
        c, d, f = i
        graph[c][d] = f
        graph[d][c] = f
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer