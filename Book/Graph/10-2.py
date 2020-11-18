# # 도시 분할 계획
# # https://www.acmicpc.net/problem/1647

# n, m = map(int, input().split())

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

# parent = [0] * (n + 1)
# edges = []
# result = 0
# edge_list = []

# for i in range(1, n + 1):
#     parent[i] = i

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     edges.append((c, a, b))

# edges.sort()

# for edge in edges:
#     c, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         edge_list.append(c)

# edge_list.remove(max(edge_list))
# result = sum(edge_list)
# print(result)




# 풀이

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

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)