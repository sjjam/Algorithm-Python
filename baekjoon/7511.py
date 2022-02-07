# 소셜 네트워킹 어플리케이션
# https://www.acmicpc.net/problem/7511

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

for t in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parent[i] = i
    
    for _ in range(int(input())):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    
    print('Scenario % s:' % (t + 1))
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if find_parent(parent, u) == find_parent(parent, v):
            print(1)
        else:
            print(0)
    print()