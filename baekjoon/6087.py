# 레이저 통신
# r1 x
# https://www.acmicpc.net/problem/6087

# https://copy-driven-dev.tistory.com/entry/%EB%B0%B1%EC%A4%80Python6087BFS%EB%A0%88%EC%9D%B4%EC%A0%80-%ED%86%B5%EC%8B%A0

from collections import deque

def search(x, y):
    global result
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited[x][y] = 0

    q = deque()
    for i in range(4):
        q.append((x, y, i, 0))

    while q:
        now = q.popleft()
        
        if now[0] == pos[1][0] and now[1] == pos[1][1]:
            result = min(result, now[3])
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            cnt = now[3]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if data[nx][ny] == '*':
                continue

            if now[2] != i:
                cnt += 1

            if visited[nx][ny] >= cnt:
                visited[nx][ny] = cnt
                q.append((nx, ny, i, cnt))

w, h = map(int, input().split())
INF = int(1e9)
data = []
for _ in range(h):
    data.append(list(input()))
pos = []
result = INF

for i in range(h):
    for j in range(w):
        if data[i][j] == 'C':
            pos.append((i, j))

visited = [[INF] * w for _ in range(h)]
search(pos[0][0], pos[0][1])
print(result)



# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-6087%EB%B2%88-%EB%A0%88%EC%9D%B4%EC%A0%80-%ED%86%B5%EC%8B%A0-1-Python

from collections import deque

def search(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while True:
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    break
                if data[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break

                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]

w, h = map(int, input().split())
INF = int(1e9)
data = []
for _ in range(h):
    data.append(list(input()))
pos = []
result = INF

for i in range(h):
    for j in range(w):
        if data[i][j] == 'C':
            pos.append((i, j))

visited = [[INF] * w for _ in range(h)]
sx, sy = pos[0]
fx, fy = pos[1]
search(sx, sy)
print(visited[fx][fy] - 1)