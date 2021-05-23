# 양
# https://www.acmicpc.net/problem/3184

from collections import deque

def check(data, visited, now):
    q = deque()
    q.append((now[0], now[1]))
    visited[now[0]][now[1]] = True
    cnt_o = 0
    cnt_v = 0
    
    while q:
        x, y = q.popleft()
        if data[x][y] == 'o':
            cnt_o += 1
        if data[x][y] == 'v':
            cnt_v += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if data[nx][ny] != '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    
    return cnt_o, cnt_v

r, c = map(int, input().split())
data = []
for _ in range(r):
    data.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * c for _ in range(r)]
result = [0, 0]

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (data[i][j] == 'o' or data[i][j] == 'v'):
            cnt_o, cnt_v = check(data, visited, (i, j))
            if cnt_o > cnt_v:
                result[0] += cnt_o
            else:
                result[1] += cnt_v

print(result[0], result[1])