# 군사 이동
# https://www.acmicpc.net/problem/11085

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

p, w = map(int ,input().split())
c, v = map(int, input().split())
parent = [0] * p

for i in range(p):
    parent[i] = i

edges = []
for _ in range(w):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=True)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    if find_parent(parent, c) == find_parent(parent, v):
        print(cost)
        break