# 자원 캐기
# https://www.acmicpc.net/problem/14430

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

temp = [[0] * m for _ in range(n)]
temp[0][0] = arr[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            temp[i][j] = temp[i][j - 1] + arr[i][j]
        elif j == 0:
            temp[i][j] = temp[i - 1][j] + arr[i][j]
        else:
            temp[i][j] = max(temp[i - 1][j], temp[i][j - 1]) + arr[i][j]

print(temp[n - 1][m - 1])