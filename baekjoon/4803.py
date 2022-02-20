# 트리
# https://www.acmicpc.net/problem/4803

# https://nbalance97.tistory.com/154
# https://vitriol95.github.io/posts/boj4803/

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
case = 1

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break
    
    parent = [0] * (n + 1)
    cycle = []

    for i in range(1, n + 1):
        parent[i] = i
    
    for i in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            cycle.append(a)
        else:
            union_parent(parent, a, b)
    
    for i in range(1, n + 1):
        find_parent(parent, i)
    
    print(parent)
    cycle_group = set()
    for i in cycle:
        cycle_group.add(parent[i])
    
    ans = 0
    for i in range(1, n + 1):
        if parent[i] not in cycle_group:
            cycle_group.add(parent[i])
            ans += 1

    if ans == 0:
        print('Case %s: No trees.' %case)
    elif ans == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {ans} trees.')
    
    case += 1