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

# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# ans = 1
# while True:
#     check = 0
#     arr[x][y] = 2
#     for i in range(4):
#         d = (d - 1) % 4
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 0:
#                 x, y = nx, ny
#                 ans += 1
#                 break
#         else:
#             if i == 3:
#                 x = x - dx[d]
#                 y = y - dy[d]
#                 if arr[x][y] == 1:
#                     check = 1
    
#     if check == 1:
#         break

# print(ans)



# 럭키 스트레이트
# r1
# https://www.acmicpc.net/problem/18406

# n = int(input())
# str_n = str(n)
# mid = len(str_n) // 2
# l = str_n[:mid]
# r = str_n[mid:]

# sum_l = 0
# sum_r = 0
# for i in l:
#     sum_l += int(i)
# for i in r:
#     sum_r += int(i)

# if sum_l == sum_r:
#     print('LUCKY')
# else:
#     print('READY')



# 문자열 재정렬
# r1

# s = input()
# alpha = []
# number = []
# ans = ''

# for i in s:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         number.append(int(i))

# alpha.sort()

# for i in alpha:
#     ans += i
# ans += str(sum(number))

# print(ans)



# 문자열 압축
# r1
# https://programmers.co.kr/learn/courses/30/lessons/60057

# def solution(s):
#     answer = 0
#     length = len(s) // 2
#     min_l = len(s)

#     for i in range(1, length + 1):
#         tmp = ''
#         cnt = 1
#         for j in range(0, len(s), i):
#             if s[j:j + i] == s[j + i:j + i + i]:
#                 cnt += 1
#             else:
#                 if cnt == 1:
#                     tmp += s[j:j + i]
#                 else:
#                     tmp += str(cnt) + s[j:j + i]
#                     cnt = 1
#         if len(tmp) < min_l:
#             min_l = len(tmp)
    
#     answer = min_l
#     return answer



# 자물쇠와 열쇠
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/60059

# def rotate_a_matrix_by_90_degree(a):
#     n = len(a)
#     m = len(a[0])
#     result = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n - i - 1] = a[i][j]
#     return result

# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length, lock_length * 2):
#         for j in range(lock_length, lock_length * 2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0] * (n * 3) for _ in range(n * 3)]

#     for i in range(n):
#         for j in range(n):
#             new_lock[i + n][j + n] = lock[i][j]
    
#     for rotation in range(4):
#         key = rotate_a_matrix_by_90_degree(key)
#         for x in range(n * 2):
#             for y in range(n * 2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y + j] += key[i][j]
                
#                 if check(new_lock) == True:
#                     return True
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y + j] -= key[i][j]
#     return False



# 뱀
# r1 x
# https://www.acmicpc.net/problem/3190

# from collections import deque

# n = int(input())
# k = int(input())
# arr = [[0] * n for _ in range(n)]
# for _ in range(k):
#     a, b = map(int, input().split())
#     arr[a - 1][b - 1] = 2
# l = int(input())
# change = []
# for _ in range(l):
#     x, d = input().split()
#     change.append((x, d))

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# idx = 0
# snake = deque()
# snake.append([0, 0])
# arr[0][0] = 1
# time = 0

# while True:
#     x, y = snake.pop()
#     nx = x + dx[idx]
#     ny = y + dy[idx]

#     if nx < 0 or nx >= n or ny < 0 or ny >= n:
#         time += 1
#         break
#     if arr[nx][ny] == 1:
#         time += 1
#         break
    
#     if arr[nx][ny] == 0:
#         arr[nx][ny] = 1
#         snake.append([x, y])
#         snake.append([nx, ny])
#         px, py = snake.popleft()
#         arr[px][py] = 0
#     if arr[nx][ny] == 2:
#         arr[nx][ny] = 1
#         snake.append([x, y])
#         snake.append([nx, ny])

#     time += 1
#     for x, d in change:
#         if int(x) == time:
#             if d == 'D':
#                 idx = (idx + 1) % 4
#             elif d == 'L':
#                 idx = (idx - 1) % 4

# print(time)

# n = int(input())
# k = int(input())
# data = [[0] * (n + 1) for _ in range(n + 1)]
# info = []

# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1

# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1
#     data[x][y] = 2
#     direction = 0
#     time = 0
#     index = 0
#     q = [(x, y)]
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]

#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
            
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         else:
#             time += 1
#             break

#         x, y = nx, ny
#         time += 1
#         if index < l and time == info[index][0]:
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time

# print(simulate())



# 기둥과 보 설치
# r1
# https://programmers.co.kr/learn/courses/30/lessons/60061

# def check(answer, x, y, a):
#     if a == 0:
#         if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
#             return True
#     elif a == 1:
#         if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
#             return True
#     return False

# def solution(n, build_frame):
#     answer = []
#     for i in build_frame:
#         x, y, a, b = i
#         if b == 1:
#             if check(answer, x, y, a):
#                 answer.append([x, y, a])
#         else:
#             answer.remove([x, y, a])
#             for j in answer:
#                 jx, jy, ja = j
#                 if not check(answer, jx, jy, ja):
#                     answer.append([x, y, a])
#                     break
            
#     answer.sort()
#     return answer



# 치킨 배달
# r1
# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
chicken = []
home = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 2:
            chicken.append((i, j))
        elif data[j] == 1:
            home.append((i, j))

choose = list(combinations(chicken, m))
ans = 1e9

for i in choose:
    result = 0
    for j in home:
        dis = n + n
        for k in i:
            dis = min(dis, abs(j[0] - k[0]) + abs(j[1] - k[1]))
        result += dis
    ans = min(ans, result)

print(ans)