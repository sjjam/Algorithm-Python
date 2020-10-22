# 음료수 얼려 먹기

from collections import deque

n, m = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int, input())))
cnt = []

def bfs(box, x, y, visited):
    global count
    now = (x, y)
    queue = deque()
    queue.append(now)
    visited[x][y] = True
    while queue:
        point = queue.popleft()
        a = point[0]
        b = point[1]
        # print(a, b)
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >=0 and nx < n and ny >=0 and ny < m:
                if box[nx][ny] == 0 and visited[nx][ny] == False:
                    next = (nx, ny)
                    queue.append(next)
                    visited[nx][ny] = True
                    count += 1
        

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and visited[i][j] == False:
            count = 1
            bfs(box, i, j, visited)
            cnt.append(count)
            count = 1

# print(cnt)
print(len(cnt))


# 풀이

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)