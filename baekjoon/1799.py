# 비숍
# r1 x
# https://www.acmicpc.net/problem/1799

# from itertools import combinations

# def check(possible):
#     for i in range(len(possible), -1, -1):
#         for j in list(combinations(possible, i)):
#             if promising(j):
#                 return i
#     return 0

# def promising(pos):
#     for i in pos:
#         for j in pos:
#             if i != j:
#                 if abs(i[0] - j[0]) == abs(i[1] - j[1]):
#                     return False
#     return True

# n = int(input())
# ans = 0
# possible = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(n):
#         if data[j] == 1:
#             possible.append((i, j))

# ans = check(possible)
# print(ans)




# https://pangsblog.tistory.com/84

def b_check(visited, x, y, cnt):
    global b_cnt
    b_cnt = max(b_cnt, cnt)
    if y >= len(visited):
        x += 1
        if x % 2 == 0:
            y = 0
        else:
            y = 1
    
    if x >= len(visited):
        return
    
    if possible(visited, x, y):
        visited[x][y] = True
        b_check(visited, x, y + 2, cnt + 1)
        visited[x][y] = False
    
    b_check(visited, x, y + 2, cnt)

def w_check(visited, x, y, cnt):
    global w_cnt
    w_cnt = max(w_cnt, cnt)
    if y >= len(visited):
        x += 1
        if x % 2 == 0:
            y = 1
        else:
            y = 0
    
    if x >= len(visited):
        return
    
    if possible(visited, x, y):
        visited[x][y] = True
        w_check(visited, x, y + 2, cnt + 1)
        visited[x][y] = False
    
    w_check(visited, x, y + 2, cnt)

def possible(visited, x, y):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    if array[x][y] == 0:
        return False
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        for j in range(len(visited)):
            if nx >= 0 and nx < len(visited) and ny >= 0 and ny < len(visited):
                if visited[nx][ny]:
                    return False
                
                nx += dx[i]
                ny += dy[i]
    return True

n = int(input())
b_cnt = 0
w_cnt = 0
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

black = [[False] * n for _ in range(n)]
b_check(black, 0, 0, 0)
white = [[False] * n for _ in range(n)]
w_check(white, 0, 1, 0)

print(b_cnt + w_cnt)