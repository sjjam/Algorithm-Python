# 전력난
# https://www.acmicpc.net/problem/6497

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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [0] * m
    edges = []
    result = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        result += c
        edges.append((c, a, b))

    for i in range(m):
        parent[i] = i

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result -= cost

    print(result)