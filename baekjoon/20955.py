# 민서의 응급 수술
# https://www.acmicpc.net/problem/20955

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

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
cnt = set()
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        result += 1

for i in range(1, n + 1):
    find_parent(parent, i)
    cnt.add(parent[i])

print(result + len(cnt) - 1)