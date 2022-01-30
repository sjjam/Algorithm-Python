# 양 구출 작전
# r1 x
# https://www.acmicpc.net/problem/16437

import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
graph = [[0, []] for _ in range(n + 1)]

for i in range(2, n + 1):
    a, b, c = input().split()
    if a == 'W':
        b = -int(b)
    graph[i][0] = int(b)
    graph[int(c)][1].append(i)

def dfs(now):
    ans = graph[now][0]
    for next in graph[now][1]:
        ans += dfs(next)
    
    if ans < 0:
        return 0
    else:
        return ans

print(dfs(1))