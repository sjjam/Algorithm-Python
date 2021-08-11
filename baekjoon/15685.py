# 드래곤 커브
# r1 x
# https://www.acmicpc.net/problem/15685


# https://jjangsungwon.tistory.com/57
# https://chldkato.tistory.com/150

import sys

input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
arr = [[0] * 101 for _ in range(101)]
n = int(input())
for _ in range(n):
    y, x, d, g = map(int, input().split())
    arr[x][y] = 1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1] + 1) % 4)
        move.extend(temp)
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            if arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
                ans += 1
print(ans)