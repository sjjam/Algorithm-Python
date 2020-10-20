# 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())
board = [[0]*n for i in range(m)]
ans = 1

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        board[i][j] = x[j]

def search(a, b, d):
    global ans
    board[a][b] = 1
    nd = [0, 1, 2, 3]
    nx = a
    ny = b
    for i in nd:
        if i == 0:
            nx = a
            ny = b - 1
        elif i == 1:
            nx = a - 1
            ny = b
        elif i == 2:
            nx = a
            ny = b + 1
        else:
            nx = a + 1
            ny = b
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if board[nx][ny] == 0:
                ans += 1
                search(nx, ny, i)
    return ans

search(a, b, d)
print(ans)
print(board)

# 풀이
# 전형적인 시뮬레이션 문제
# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)