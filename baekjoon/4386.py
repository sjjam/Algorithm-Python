# 별자리 만들기
# https://www.acmicpc.net/problem/4386

import math

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
data = []
for i in range(n):
    x, y = map(float, input().split())
    data.append((i + 1, x, y))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        distance = math.sqrt(abs(data[i][1] - data[j][1])**2 + abs(data[i][2] - data[j][2])**2)
        edges.append((distance, data[i][0], data[j][0]))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print('%.2f' % result)