# 가장 가까운 공통 조상
# r1 x
# https://www.acmicpc.net/problem/3584

# https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-3584%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B0%80%EA%B9%8C%EC%9A%B4-%EA%B3%B5%ED%86%B5-%EC%A1%B0%EC%83%81-Python-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%83%90%EC%83%89

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a

    a, b = map(int, input().split())
    pa = [0, a]
    pb = [0, b]

    while parent[a]:
        pa.append(parent[a])
        a = parent[a]
    
    while parent[b]:
        pb.append(parent[b])
        b = parent[b]
    
    i = 1
    while pa[-i] == pb[-i]:
        i += 1
    
    print(pa, pb)
    print(pa[-i + 1])