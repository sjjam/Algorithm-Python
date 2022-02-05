# 상어 초등학교
# https://www.acmicpc.net/problem/21608

import sys
from collections import defaultdict

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(now):
    temp_x = 0
    temp_y = 0
    max_cnt = -1
    max_blank = -1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] != 0:
                continue
            cnt = 0
            blank = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx >= 1 and nx < n + 1 and ny >= 1 and ny < n + 1:
                    if arr[nx][ny] == 0:
                        blank += 1
                    else:
                        if arr[nx][ny] in like[now]:
                            cnt += 1
            
                if cnt >= max_cnt:
                    if cnt == max_cnt:
                        if blank > max_blank:
                            temp_x = i
                            temp_y = j
                            max_cnt = cnt
                            max_blank = blank
                    else:
                        temp_x = i
                        temp_y = j
                        max_cnt = cnt
                        max_blank = blank
    
    arr[temp_x][temp_y] = now

input = sys.stdin.readline
n = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
like = defaultdict(list)
order = []
ans = 0

for _ in range(n * n):
    line = list(map(int, input().split()))
    order.append(line[0])
    like[line[0]] = line[1:]

for i in order:
    check(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        now = arr[i][j]
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx >= 1 and nx < n + 1 and ny >= 1 and ny < n + 1:
                if arr[nx][ny] in like[now]:
                    cnt += 1
        
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)