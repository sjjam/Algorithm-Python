# 게임
# r1 x
# https://www.acmicpc.net/problem/1103

'''
사이클에 대해서는 같은 map 사이즈로 visited 배열을 선언해서 이전에 방문한 적이 있으면 -1을 출력 후 리턴을 하게 해주었는데, 
같은 위치를 가더라도 어디를 거쳐서 왔는지에 대해서는 다르게 처리해줄 필요가 있었다. 결국은 DP(동적 계획법)도 필요

출처: https://nemowork.com/749 [니모공작소]
https://hillier.tistory.com/65?category=973587
'''

import sys
sys.setrecursionlimit(10**6)

def move(data, dp, visited, x, y, cnt):
    global answer
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    answer = max(answer, cnt)
    for i in range(4):
        nx = x + (dx[i] * int(data[x][y]))
        ny = y + (dy[i] * int(data[x][y]))

        if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data[0]):
            if cnt + 1 > dp[nx][ny]:
                if data[nx][ny] != 'H':
                    if visited[nx][ny]:
                        print(-1)
                        exit()
                    else:
                        dp[nx][ny] += 1
                        visited[nx][ny] = True
                        move(data, dp, visited, nx, ny, cnt + 1)
                        visited[nx][ny] = False

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(str, input())))
answer = 0
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
move(data, dp, visited, 0, 0, 0)
print(answer + 1)