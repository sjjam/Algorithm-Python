# 치즈
# https://www.acmicpc.net/problem/2636

import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(cheese):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if arr[nx][ny] == 0:
                        q.append((nx, ny))
                    elif arr[nx][ny] == 1:
                        arr[nx][ny] = 2
                        cheese -= 1
    return cheese

def delete():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                arr[i][j] = 0
        

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cheese = 0
for i in range(n):
    for j in range(m):
      if arr[i][j] == 1:
          cheese += 1

before = cheese
cnt = 0
while cheese > 0:
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cheese = bfs(cheese)

    if cheese != 0:
        before = cheese
    delete()
    cnt += 1

print(cnt)
print(before)