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



from collections import deque

def water(water_area, data):
    new = []
    for i in water_area:
        for j in range(4):
            nx = i[0] + dx[j]
            ny = i[1] + dy[j]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if data[nx][ny] == '.' or data[nx][ny] == 'S':
                data[nx][ny] = '*'
                new.append((nx, ny))
    return new

def move(x, y, water_area):
    q = deque()
    q.append((x, y))
    while q:
        cnt = len(q)
        if len(water_area) != 0:
            water_area = water(water_area, data)
        while cnt:
            now_x, now_y = q.popleft()
            
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                
                if data[nx][ny] == 'D':
                    result[nx][ny] = result[now_x][now_y] + 1
                    return result[nx][ny]
                    
                if data[nx][ny] == '.' and result[nx][ny] == 0 and data[nx][ny] != 'S':
                    result[nx][ny] = result[now_x][now_y] + 1
                    q.append((nx, ny))
            cnt -= 1

r, c = map(int, input().split())
data = []
water_area = []
x, y = 0, 0
for i in range(r):
    line = list(input())
    data.append(line)
    for j in range(len(line)):
        if line[j] == 'S':
            x = i
            y = j
        if line[j] == '*':
            water_area.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = [[0] * c for _ in range(r)]
ans = move(x, y, water_area)

if ans == None:
    print('KAKTUS')
else:
    print(ans)