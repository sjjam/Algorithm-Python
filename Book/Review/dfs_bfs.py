# 5-1
# r1

# from collections import deque

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# visited = [[False] * m for _ in range(n)]
# ans = 0

# def bfs(a, b):
#     global ans
#     ans += 1
#     q = deque()
#     q.append((a, b))
#     visited[a][b] = True
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx >= 0 and nx < n and ny >=0 and ny < m:
#                 if arr[nx][ny] == 0 and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     q.append((nx, ny))

# for i in range(n):
#     for j in range(m):
#         if not visited[i][j] and arr[i][j] == 0:
#             bfs(i, j)

# print(ans)



# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1

# print(result)



# 5-2
# r1

# from collections import deque

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def bfs(a, b):
#     q = deque()
#     q.append((a, b))
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx >= 0 and nx < n and ny >=0 and ny < m:
#                 if arr[nx][ny] == 1:
#                     q.append((nx, ny))
#                     arr[nx][ny] = arr[x][y] + 1

# bfs(0, 0)
# print(arr[n - 1][m - 1])



# 특정 거리의 도시 찾기
# r1 x
# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
print(distance)
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)