# 구슬 탈출 4
# r1 x
# https://www.acmicpc.net/problem/15653

# https://rebas.kr/727

from collections import deque
import sys
sys.stdin.readline

def search(pos):
    q = deque()
    rx, ry = pos[0]
    bx, by = pos[1]
    q.append((rx, ry, bx, by, 0))
    visited.append((rx, ry, bx, by))

    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        for i in range(4):
            nx1, ny1, nx2, ny2 = x1, y1, x2, y2
            while True:
                nx1 += dx[i]
                ny1 += dy[i]
                if data[nx1][ny1] == 'O':
                    break
                if data[nx1][ny1] == '#':
                    nx1 -= dx[i]
                    ny1 -= dy[i]
                    break
            
            while True:
                nx2 += dx[i]
                ny2 += dy[i]
                if data[nx2][ny2] == 'O':
                    break
                if data[nx2][ny2] == '#':
                    nx2 -= dx[i]
                    ny2 -= dy[i]
                    break
            
            if data[nx2][ny2] == 'O':
                continue
            if data[nx1][ny1] == 'O':
                print(cnt + 1)
                return
                
            if nx1 == nx2 and ny1 == ny2:
                if abs(nx1 - x1) + abs(ny1 - y1) > abs(nx2 - x2) + abs(ny2 - y2):
                    nx1 -= dx[i]
                    ny1 -= dy[i]
                else:
                    nx2 -= dx[i]
                    ny2 -= dy[i]
            
            if (nx1, ny1, nx2, ny2) not in visited:
                visited.append((nx1, ny1, nx2, ny2))
                q.append((nx1, ny1, nx2, ny2, cnt + 1))
    print(-1)
    return


n, m = map(int, input().split())
INF = int(1e9)
data = []
for i in range(n):
    data.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
pos = [0] * 3

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            pos[0] = (i, j)
        elif data[i][j] == 'B':
            pos[1] = (i, j)
        elif data[i][j] == 'O':
            pos[2] = (i, j)

visited = []
search(pos)