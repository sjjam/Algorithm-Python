# 탈출
# https://www.acmicpc.net/problem/3055

# https://chldkato.tistory.com/22

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    result[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if data[nx][ny] == '.' and result[nx][ny] == 0:
                        result[nx][ny] = result[x][y] + 1
                        q.append([nx, ny])
                    elif data[nx][ny] == 'D':
                        print(result[x][y])
                        return
            qlen -= 1
        water()

    print("KAKTUS")
    return

def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if data[nx][ny] == '.':
                    data[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

r, c = map(int, input().split())
data = []
for i in range(r):
    data.append(list(input()))
result = [[0] * c for _ in range(r)]
q, wq = deque(), deque()

for i in range(r):
    for j in range(c):
        if data[i][j] == 'S':
            x, y = i, j
            data[i][j] = '.'
        elif data[i][j] == '*':
            wq.append([i, j])

water()
bfs(x, y)