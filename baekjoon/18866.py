# 젊은 날의 생이여
# r1 x
# https://www.acmicpc.net/problem/18866

import sys

input = sys.stdin.readline
n = int(input())
day = [[0, 0]]
youth = [[] for _ in range(n + 1)]
old = [[] for _ in range(n + 1)]
for _ in range(n):
    u, v = map(int, input().split())
    day.append([u, v])

min_u, max_u = int(10e9), -1
min_v, max_v = int(10e9), -1

for i in range(1, n + 1):
    if day[i][0] != 0 and day[i][0] < min_u:
        min_u = day[i][0]
    if day[i][1] != 0 and day[i][1] > max_v:
        max_v = day[i][1]
    youth[i] = [min_u, max_v]

for i in range(n, 0, -1):
    if day[i][0] != 0 and day[i][0] > max_u:
        max_u = day[i][0]
    if day[i][1] != 0 and day[i][1] < min_v:
        min_v = day[i][1]
    old[i] = [max_u, min_v]

cnt = -1
for i in range(n - 1, 0, -1):
    youth_u = youth[i][0]
    youth_v = youth[i][1]
    old_u = old[i + 1][0]
    old_v = old[i + 1][1]

    if youth_u > old_u and youth_v < old_v:
        if cnt < i:
            cnt = i

print(cnt)