# 레이저 통신
# https://www.acmicpc.net/problem/6087

from collections import deque

def search(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visitied = [[-1] * w for _ in range(h)] # dir 방향 지정

    q = deque()
    q.append((x, y))
    data[x][y] = 0

    while q:
        now_x, now_y = q.popleft()
        
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if data[nx][ny] == '.':
                data[nx][ny] = data[now_x][now_y] + 1
                q.append((nx, ny))
            
            if data[nx][ny] == 'C':
                data[nx][ny] = data[now_x][now_y] + 1
                return

w, h = map(int, input().split())
data = []
for _ in range(h):
    data.append(list(input()))
x = 0
y = 0

for i in range(h):
    for j in range(w):
        if data[i][j] == 'C':
            x = i
            y = j

search(x, y)

for i in range(h):
    for j in range(w):
        if data[i][j] == '*' or data[i][j] == '.' or data[i][j] < 10:
            print('*' + str(data[i][j]), end=' ')
        else:
            print(data[i][j], end=' ')
    print()