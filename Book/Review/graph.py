# 10-1
# r1

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# parent = [0] * (n + 1)

# for i in range(1, n + 1):
#     parent[i] = i

# result = []
# for i in range(m):
#     a, b, c = map(int, input().split())
#     if a == 0:
#         union_parent(parent, b, c)
#     else:
#         if find_parent(parent, b) == find_parent(parent, c):
#             print('YES')
#         else:
#             print('NO')



# 10-2
# r1
# https://www.acmicpc.net/problem/1647

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# parent = [0] * (n + 1)
# edges = []

# for i in range(1, n + 1):
#     parent[i] = i

# for i in range(m):
#     a, b, c = map(int, input().split())
#     edges.append((c, a, b))

# edges.sort()
# result = 0
# max_cost = 0

# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         max_cost = cost

# print(result - max_cost)



# 커리큘럼
# r1 x

# from collections import deque
# import copy

# n = int(input())
# indegree = [0] * (n + 1)
# time = [0] * (n + 1)
# graph = [[] for _ in range(n + 1)]

# for i in range(1, n + 1):
#     data = list(map(int, input().split()))
#     time[i] = data[0]
#     for x in data[1:-1]:
#         indegree[i] += 1
#         graph[x].append(i)

# def topology_sort():
#     result = copy.deepcopy(time)
#     q = deque()

#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append(i)
    
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             result[i] = max(result[i], result[now] + time[i])
#             indegree[i] -= 1

#             if indegree[i] == 0:
#                 q.append(i)
    
#     for i in range(1, n + 1):
#         print(result[i])

# topology_sort()



# 여행 계획
# r1

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# parent = [0] * (n + 1)
# ans = 'YES'

# for i in range(1, n + 1):
#     parent[i] = i

# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(n):
#         if data[j] == 1:
#             union_parent(parent, i + 1, j + 1)

# plan = list(map(int, input().split()))

# for i in range(len(plan) - 1):
#     if parent[plan[i]] != parent[plan[i + 1]]:
#         ans = 'NO'

# print(ans)



# 탑승구
# r1 x

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# g = int(input())
# p = int(input())
# parent = [0] * (g + 1)

# for i in range(1, g + 1):
#     parent[i] = i

# result = 0
# for i in range(p):
#     data = find_parent(parent, int(input()))
#     if data == 0:
#         break
#     union_parent(parent, data, data - 1)
#     result += 1

# print(result)



# 어두운 길
# r1

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# parent = [0] * n
# edges = []
# result = 0

# for i in range(n):
#     parent[i] = i

# for i in range(m):
#     x, y, z = map(int, input().split())
#     result += z
#     edges.append((z, x, y))

# edges.sort()

# for edge in edges:
#     cost, x, y = edge
#     if find_parent(parent, x) != find_parent(parent, y):
#         union_parent(parent, x, y)
#         result -= cost

# print(result)



# 행성 터널
# r1 x
# https://www.acmicpc.net/problem/2887

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)