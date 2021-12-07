# 숫자고르기
# r1 x
# https://www.acmicpc.net/problem/2668



# https://cotak.tistory.com/141

import sys

def dfs(u, visited):
    visited.add(u)
    check[u] = True
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    num = int(input())
    graph[num].append(i)
check = [False] * (n + 1)
result = []

for i in range(1, n + 1):
    if not check[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for i in result:
    print(i)