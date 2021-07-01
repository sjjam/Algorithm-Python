# 음악프로그램
# https://www.acmicpc.net/problem/2623

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    data = list(map(int, input().split()))
    for i in range(1, data[0]):
        graph[data[i]].append(data[i + 1])
        indegree[data[i + 1]] += 1

q = deque()
result = []

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)