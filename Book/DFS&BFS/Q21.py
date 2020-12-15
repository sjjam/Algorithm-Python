# 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = True
    temp = []
    temp.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny] and abs(country[x][y] - country[nx][ny]) >= l and abs(country[x][y] - country[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    temp.append((nx, ny))
    if len(temp) >= 2:
        pop = 0
        for i in temp:
            pop += country[i[0]][i[1]]
        pop_a = pop // len(temp)

        for i in temp:
            country[i[0]][i[1]] = pop_a

def chk(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >= 0 and ny < n:
                if abs(country[x][y] - country[nx][ny]) >= l and abs(country[x][y] - country[nx][ny]) <= r:
                    return True
    return False

ans = 0
while True:
    check = False
    for i in range(n):
        for j in range(n):
            if chk(i, j):
                check = True
                break
        if check:
            break

    if check == False:
        break

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)    
    ans += 1

print(ans)






# 풀이

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    total_count += 1

print(total_count)