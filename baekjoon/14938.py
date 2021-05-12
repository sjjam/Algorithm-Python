# 서강그라운드
# https://www.acmicpc.net/problem/14938

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
ans = 0

for i in range(r):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

for i in range(len(graph)):
    for j in range(len(graph)):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    sum_item = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            sum_item += item[j - 1]
    ans = max(ans, sum_item)

print(ans)