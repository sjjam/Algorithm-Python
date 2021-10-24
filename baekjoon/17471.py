# 게리맨더링
# https://www.acmicpc.net/problem/17471


# https://cotak.tistory.com/66

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs(case):
    start = case[0]
    q = deque([start])
    visited = [start]
    sum = 0
    
    while q:
        v = q.popleft()
        sum += num[v]

        for i in graph[v]:
            if i not in visited and i in case:
                q.append(i)
                visited.append(i)

    return sum, len(visited)

n = int(input())
num = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
result = 1000

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(1, len(line)):
        graph[i + 1].append(line[j])

for i in range(1, n // 2 + 1):
    com = list(combinations(range(1, n + 1), i))
    
    for j in com:
        sum1, v1 = bfs(j)
        g2 = []
        for k in range(1, n + 1):
            if k not in j:
                g2.append(k)
        sum2, v2 = bfs(g2)

        if v1 + v2 == n:
            result = min(result, abs(sum1 - sum2))

if result == 1000:
    print(-1)
else:
    print(result)