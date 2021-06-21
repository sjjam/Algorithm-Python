# 골목 대장 호석 - 효율성 2
# r1 x
# https://www.acmicpc.net/problem/20183

# python3 시간초과, pypy 부분성공

import heapq
import sys

sys.stdin.readline
INF = int(1e9)

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start, mid):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if i[1] > mid:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    if distance[b] <= c:
        return True
    return False

# dijkstra(a)
start = 1
end = c
answer = INF

while start <= end:
    mid = (start + end) // 2
    if dijkstra(a, mid):
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

if answer == INF:
    print(-1)
else:
    print(answer)