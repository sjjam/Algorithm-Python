# 침투
# https://www.acmicpc.net/problem/13565

import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    if x == m - 1:
        return True
    data[x][y] = '-1'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny <0 or ny >= n:
            continue

        if data[nx][ny] == '0':
            if dfs(nx, ny):
                return True
    return False

m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(input()))
result = False

for i in range(n):
    if data[0][i] == '0':
        result = dfs(0, i)
        if result:
            break

if result:
    print('YES')
else:
    print('NO')



from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    data[x][y] = '-1'
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue

            if data[nx][ny] == '0':
                data[nx][ny] = '-1'
                q.append((nx, ny))


m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(input()))

for i in range(n):
    if data[0][i] == '0':
        bfs(0, i)

result = 'NO'
if '-1' in data[m - 1]:
    result = 'YES'

print(result)