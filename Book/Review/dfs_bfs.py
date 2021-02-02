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

# from collections import deque

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# distance = [-1] * (n + 1)
# distance[x] = 0

# q = deque([x])
# while q:
#     now = q.popleft()
#     for next_node in graph[now]:
#         if distance[next_node] == -1:
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)

# check = False
# print(distance)
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True

# if check == False:
#     print(-1)



# 연구소
# r1
# https://www.acmicpc.net/problem/14502

# from itertools import combinations
# from collections import deque
# import copy

# n, m = map(int, input().split())
# arr = []
# virus = []
# none = []

# for i in range(n):
#     data = list(map(int, input().split()))
#     arr.append(data)
#     for j in range(len(data)):
#         if data[j] == 2:
#             virus.append((i, j))
#         if data[j] == 0:
#             none.append((i, j))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# safe = 0

# def spread(tmp):
#     for i in virus:
#         q = deque()
#         x, y = i
#         q.append((x, y))

#         while q:
#             x, y = q.popleft()
#             for j in range(4):
#                 nx = x + dx[j]
#                 ny = y + dy[j]

#                 if nx >= 0 and nx < n and ny >=0 and ny < m:
#                     if tmp[nx][ny] == 0:
#                         tmp[nx][ny] = 2
#                         q.append((nx, ny))

# ans = 0

# for i in list(combinations(none, 3)):
#     tmp = copy.deepcopy(arr)
#     for j in i:
#         tmp[j[0]][j[1]] = 1
    
#     spread(tmp)
#     cnt = 0
    
#     for j in range(n):
#         for k in range(m):
#             if tmp[j][k] == 0:
#                 cnt += 1
    
#     ans = max(ans, cnt)

# print(ans)



# 경쟁적 전염
# r1 x
# https://www.acmicpc.net/problem/18405

# from collections import deque

# n, k = map(int, input().split())

# graph = []
# data = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] != 0:
#             data.append((graph[i][j], 0, i, j))

# data.sort()
# q = deque(data)

# target_s, target_x, target_y = map(int, input().split())

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# while q:
#     virus, s, x, y = q.popleft()
#     if s == target_s:
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx and nx < n and 0 <= ny and ny < n:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s + 1, nx, ny))

# print(graph[target_x - 1][target_y - 1])



# 괄호 변환
# r1
# https://programmers.co.kr/learn/courses/30/lessons/60058

def step(p):
    u = ''
    v = ''
    cnt_l = 0
    cnt_r = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt_l += 1
        else:
            cnt_r += 1
        if cnt_l != 0 and cnt_l == cnt_r:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if len(u) != 0:
        if u[0] == '(':
            u += step(v)
        else:
            tmp = '('
            tmp += step(v)
            tmp += ')'
            tmp2 = ''
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    tmp2 += ')'
                else:
                    tmp2 += '('
            tmp += tmp2
            return tmp
    return u

def solution(p):
    answer = ''
    if p == '':
        answer = ''
    else:
        answer = step(p)

    return answer