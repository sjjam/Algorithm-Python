# 공항
# https://www.acmicpc.net/problem/10775

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

g = int(input())
p = int(input())
parent = [0] * (g + 1)
result = 0

for i in range(1, g + 1):
    parent[i] = i

for i in range(p):
    data = int(input())
    now = find_parent(parent, data)
    if now == 0:
        break
    union_parent(parent, now, now - 1)
    result += 1

print(result)