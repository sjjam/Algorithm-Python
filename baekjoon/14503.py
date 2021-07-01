# 로봇 청소기
# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

def clean(x, y, d):
    global answer

    if data[x][y] == 0:
        answer += 1
        data[x][y] = 2
    
    for _ in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if data[nx][ny] == 0:
            clean(nx, ny, d)
            return
    
    nx = x - dx[d]
    ny = y - dy[d]
    if data[nx][ny] == 1:
        return
    clean(nx, ny, d)

n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

clean(x, y, d)
print(answer)