# 내리막 길
# https://www.acmicpc.net/problem/1520

import sys
import heapq

def bfs(x, y, h):
	q = []
	heapq.heappush(q, (-h, x, y))
	q.append((x, y, h))
	visited = [[0] * n for _ in range(m)]
	visited[0][0] = 1

	while q:
		now_h, now_x, now_y = heapq.heappop(q)
		now_h *= -1
		if now_x == m - 1 and now_y == n - 1:
			continue

		for i in range(4):
			nx = now_x + dx[i]
			ny = now_y + dy[i]

			if nx < 0 or nx >= m or ny < 0 or ny >= n:
				continue
			if arr[nx][ny] < now_h:
				if visited[nx][ny] == 0:
					heapq.heappush(q, (-arr[nx][ny], nx, ny))
				visited[nx][ny] += visited[now_x][now_y]

	return visited[m - 1][n - 1]

input = sys.stdin.readline
m, n = map(int, input().split())
arr = []
for _ in range(m):
	arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(bfs(0, 0, arr[0][0]))