# 4-1
# r1

# n = int(input())
# data = input().split()

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# x, y = 1, 1
# for i in data:
#     direction = -1
#     if i == 'L':
#         direction = 0
#     elif i == 'U':
#         direction = 1
#     elif i == 'R':
#         direction = 2
#     else:
#         direction = 3
#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     if nx >= 1 and ny <= n and ny >= 1 and ny <= n:
#         x = nx
#         y = ny

# print(x, y)



# 4-2
# r1

# n = int(input())
# h = 0
# m = 0
# s = 0
# ans = 0

# while True:
#     s += 1
#     if s == 60:
#         s = 0
#         m += 1
#     if m == 60:
#         m = 0
#         h += 1
#     time = f'{h}시 {m}분 {s}초'
    
#     if '3' in time:
#         ans += 1

#     if time == f'{n}시 59분 59초':
#         break

# print(ans)



# 4-3
# r1

# p = input()
# move = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1)]
# arr = [[0] * 8 for _ in range(8)]

# row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# x = row.index(p[0]) + 1
# y = int(p[1])

# ans = 0
# for m in move:
#     a, b = m
#     nx = x + a
#     ny = y + b
#     if nx >= 1 and nx < 9 and ny >= 1 and ny < 9:
#         ans += 1

# print(ans)



# 4-4
# r1

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 1
while True:
    check = 0
    arr[x][y] = 2
    for i in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 0:
                x, y = nx, ny
                ans += 1
                break
        else:
            if i == 3:
                x = x - dx[d]
                y = y - dy[d]
                if arr[x][y] == 1:
                    check = 1
    
    if check == 1:
        break

print(ans)