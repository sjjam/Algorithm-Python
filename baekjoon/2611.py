# 자동차경주
# https://www.acmicpc.net/problem/2611


# https://ksj14.tistory.com/entry/BaekJoon2611-%EC%9E%90%EB%8F%99%EC%B0%A8-%EA%B2%BD%EC%A3%BC

# 실패

# import sys
# from collections import deque

# def check(now):
#     for i in visited[now]:
#         if i[0] == 1:
#             if 0 == result[now] - i[1]:
#                 route.append(i[0])
#         else:
#             if result[i[0]] == result[now] - i[1]:
#                 route.append(i[0])
#                 check(i[0])

# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# indegree = [0] * (n + 1)
# for _ in range(m):
#     p, q, r = map(int, input().split())
#     graph[p].append((q, r))
#     indegree[q] += 1

# q = deque()
# q.append((1))
# result = [0] * (n + 1)
# route = []
# visited = [[] for _ in range(n + 1)]

# while q:
#     now = q.popleft()
#     if now == 1 and result[1] != 0:
#         break
    
#     for i in graph[now]:
#         indegree[i[0]] -= 1
#         visited[i[0]].append((now, i[1]))
#         if result[now] + i[1] > result[i[0]]:
#             result[i[0]] = result[now] + i[1]
            
#         if indegree[i[0]] == 0:
#             q.append((i[0]))

# print(result[1])
# check(1)
# route.reverse()
# print(*route)



# 시간초과

# import heapq
# import sys

# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [0] * (n + 1)
# for _ in range(m):
#     p, q, r = map(int, input().split())
#     graph[p].append((q, r))
# road = [0] * (n + 1)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)
#         dist = -dist
#         if distance[now] > dist:
#             continue

#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] < cost:
#                 distance[i[0]] = cost
#                 road[i[0]] = now
#                 if i[0] != start:
#                     heapq.heappush(q, (-cost, i[0]))

# def route(now):
#     if road[now] == 1:
#         print(1, end=' ')
#         print(now, end=' ')
#         return
    
#     route(road[now])
#     print(now, end=' ')

# dijkstra(1)
# print(distance[1])
# print(road)
# route(1)



# 정답

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    indegree[q] += 1

q = deque()
q.append((1))
result = [0] * (n + 1)
road = [0] * (n + 1)
visited = [[] for _ in range(n + 1)]

while q:
    now = q.popleft()
    if now == 1 and result[1] != 0:
        break
    
    for i in graph[now]:
        indegree[i[0]] -= 1
        visited[i[0]].append((now, i[1]))
        if result[now] + i[1] > result[i[0]]:
            result[i[0]] = result[now] + i[1]
            road[i[0]] = now
            
        if indegree[i[0]] == 0:
            q.append((i[0]))

def route(now):
    if road[now] == 1:
        print(1, end=' ')
        print(now, end=' ')
        return
    
    route(road[now])
    print(now, end=' ')

print(result[1])
route(1)