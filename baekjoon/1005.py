# ACM Craft
# https://www.acmicpc.net/problem/1005

from collections import deque
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    delay = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    target = int(input())
    result = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            result[i] = delay[i - 1]
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[now] + delay[i - 1], result[i])
            if indegree[i] == 0:
                q.append(i)

    print(result[target])