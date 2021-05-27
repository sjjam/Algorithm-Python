# 양치기 꿍
# https://www.acmicpc.net/problem/3187

import sys
sys.setrecursionlimit(50000)

def check(data, visited, x, y):
    visited[x][y] = True
    cnt_v = 0
    cnt_k = 0
    if data[x][y] == 'v':
        cnt_v += 1
    elif data[x][y] == 'k':
        cnt_k += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if data[nx][ny] != '#' and not visited[nx][ny]:
            cnt_next = check(data, visited, nx, ny)
            cnt_v += cnt_next[0]
            cnt_k += cnt_next[1]
    return cnt_v, cnt_k


r, c = map(int, input().split())
data = []
for _ in range(r):
    data.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * c for _ in range(r)]
result = [0, 0]

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (data[i][j] == 'v' or data[i][j] == 'k'):
            cnt_v, cnt_k = check(data, visited, i, j)
            if cnt_v < cnt_k:
                result[0] += cnt_k
            else:
                result[1] += cnt_v

print(result[0], result[1])