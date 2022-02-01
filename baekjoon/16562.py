# 친구비
# https://www.acmicpc.net/problem/16562

import sys

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

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    v, w = map(int, input().split())
    union_parent(parent, v, w)

dic = dict()
ans = 0
for i in range(1, n + 1):
    p = find_parent(parent, i)
    cost = arr[i]

    if p not in dic:
        dic[p] = 10000
    
    if dic[p] > cost:
        dic[p] = cost

for i in list(dic.keys()):
    ans += dic[i]

if ans <= k:
    print(ans)
else:
    print('Oh no')