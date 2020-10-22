# 미로 탈출

from collections import deque

n, m = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input())))

def bfs(miro, x, y, visited):
    queue = deque()
    now = (x, y)
    queue.append(now)
    visited[x][y] = True
    miro[x][y] = 1
    while queue:
        point = queue.popleft()
        a = point[0]
        b = point[1]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if miro[nx][ny] == 1 and visited[nx][ny] == False:
                    next = (nx, ny)
                    queue.append(next)
                    visited[nx][ny] = True
                    miro[nx][ny] = miro[a][b] + 1

visited = [[False] * m for _ in range(n)]

bfs(miro, 0, 0, visited)
# print(miro)
print(miro[n - 1][m - 1])


# 풀이

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))