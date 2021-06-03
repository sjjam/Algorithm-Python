# Strahler 순서
# https://www.acmicpc.net/problem/9470

from collections import deque

for _ in range(int(input())):
    k, m, p = map(int, input().split())
    indegree = [0] * (m + 1)
    graph = [[] for _ in range(m + 1)]

    for i in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    result = [[] for _ in range(m + 1)]
    s = 0
    q = deque()

    for i in range(1, m + 1):
        if indegree[i] == 0:
            result[i].append(1)
            q.append(i)

    while q:
        now = q.popleft()
        s = max(result[now])
        if result[now].count(s) >= 2:
            s += 1

        for i in graph[now]:
            indegree[i] -= 1
            result[i].append(s)
            if indegree[i] == 0:
                q.append(i)
    
    print(k, s)