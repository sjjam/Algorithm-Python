# 전기가 부족해
# https://www.acmicpc.net/problem/10423

import sys

input = sys.stdin.readline

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

n, m, k = map(int, input().split())
power = list(map(int, input().split()))
parent = [0] * (n + 1)

for i in range(1, n + 1):
    if i in power:
        continue
    parent[i] = i

edges = []

for _ in range(m):
    u, v, c = map(int, input().split())
    edges.append((c, u, v))

edges.sort()
result = 0

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)