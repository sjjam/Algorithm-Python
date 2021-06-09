# 섬의 개수
# https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10**9)

def search(data, x, y):
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 1]
    data[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
            continue
        
        if data[nx][ny] == 1:
            search(data, nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    data = []
    result = 0

    for _ in range(h):
        data.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1:
                search(data, i, j)
                result += 1
    
    print(result)