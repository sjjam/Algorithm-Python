# 뱀
# https://www.acmicpc.net/problem/3190

# from collections import deque

# n = int(input())
# k = int(input())
# arr = [[0] * n for _ in range(n)]

# for _ in range(k):
#     a, b = map(int, input().split())
#     arr[a - 1][b - 1] = 1

# l = int(input())
# move = []

# for _ in range(l):
#     x, c = input().split()
#     move.append((int(x), c))

# time = 0
# nx = 0
# ny = 0
# q = deque()
# dir_all = ['r', 'd', 'l', 'u']
# dir_idx = 0
# move_idx = 0
# q.append((nx, ny))

# while True:
#     time += 1
#     if move_idx < len(move) and time - 1 == move[move_idx][0]:
#         if move[move_idx][1] == 'D':
#             dir_idx += 1
#         else:
#             dir_idx -= 1
#         if dir_idx == 4:
#             dir_idx = 0
#         elif dir_idx == -1:
#             dir_idx = 3
#         move_idx += 1
#     dir_n = dir_all[dir_idx]
    
#     if dir_n == 'r':
#         ny += 1
#     elif dir_n == 'd':
#         nx += 1
#     elif dir_n == 'l':
#         ny -= 1
#     else:
#         nx -= 1
    
#     if nx < 0 or ny < 0 or nx >= n or ny >= n:
#         break
    
#     if (nx, ny) in q:
#         break

#     q.append((nx, ny))
#     now = arr[nx][ny]
#     if now != 1:
#         q.popleft()

# print(time)





# 풀이

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())