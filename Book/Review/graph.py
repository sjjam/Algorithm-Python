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

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = 0
max_cost = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)