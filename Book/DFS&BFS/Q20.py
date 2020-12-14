# 감시 피하기
# https://www.acmicpc.net/problem/18428

from itertools import combinations
import copy

n = int(input())
arr = []
blank = []
teacher = []
for i in range(n):
    data = list(input().split())
    arr.append(data)
    for j in range(len(data)):
        if data[j] == 'X':
            blank.append((i, j))
        elif data[j] == 'T':
            teacher.append((i, j))

point = list(combinations(blank, 3))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def search(temp, x, y):
    result = 'NO'
    for i in range(4):
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if temp[nx][ny] == 'O':
                break
            if temp[nx][ny] == 'S':
                result = 'YES'
                break
    return result

ans = 'NO'
for i in point:
    temp = copy.deepcopy(arr)
    chk = ''
    for j in i:
        temp[j[0]][j[1]] = 'O'
    for j in teacher:
        if search(temp, j[0], j[1]) == 'NO':
            chk += 'N'
    if chk == 'N' * len(teacher):
        ans = 'YES'
        break

print(ans)




# 풀이

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')