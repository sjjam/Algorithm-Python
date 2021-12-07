# 회장뽑기
# https://www.acmicpc.net/problem/2660

import sys

input = sys.stdin.readline
n = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

can = []
min_score = INF
for i in range(1, n + 1):
    min_score = min(min_score, max(graph[i][1:]))
for i in range(1, n + 1):
    if min_score == max(graph[i][1:]):
        can.append(i)
can.sort()
print(min_score, len(can))
for i in can:
    print(i, end=' ')