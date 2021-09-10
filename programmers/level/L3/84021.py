# 퍼즐 조각 채우기
# https://programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def search(table, x, y, div):
    result = []
    if div == 't':
        num = 1
    else:
        num = 0
    
    q = deque()
    q.append((x, y))
    result.append((x, y))
    table[x][y] = -1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < len(table) and ny >= 0 and ny < len(table):
                if table[nx][ny] == num:
                    q.append((nx, ny))
                    result.append((nx, ny))
                    table[nx][ny] = -1
    return result

def rot(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = arr[i][j]
    return result

def solution(game_board, table):
    answer = -1
    board_void = []
    puzzle = []
    
    for i in range(len(table)):
        for j in range(len(table)):
            if game_board[i][j] == 0:
                board_void.append(search(game_board, i, j, 'g'))
    print(board_void)
    
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                puzzle.append(search(table, i, j, 't'))
    print(puzzle)

    for i in board_void:
        check = True
        for j in puzzle:
            puzzle_result = [[0] * len(table) for _ in range(len(table))]
            for k in j:
                puzzle_result[k[0]][k[1]] = 1
            print(puzzle_result)

            if len(i) == len(j):
                x = abs(i[0][0] - j[0][0])
                y = abs(i[0][1] - j[0][1])
                for l in range(len(i)):
                    if abs(i[l][0] - j[l][0]) != x or abs(i[l][1] - j[l][1]) != y:
                        check = False
                        break
        
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])