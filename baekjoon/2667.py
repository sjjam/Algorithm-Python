# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt = 0

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny]:
                arr[nx][ny] = -1
                q.append((nx, ny))
    return cnt

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))
ans = []

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            ans.append(bfs(i, j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)