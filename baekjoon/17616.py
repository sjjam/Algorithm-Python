# 등수 찾기
# r1 x
# https://www.acmicpc.net/problem/17616

# https://home-body.tistory.com/646

from collections import deque
import sys

def check(x, arr):
    cnt = 0
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        now = q.popleft()
        for i in arr[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

    return cnt

input = sys.stdin.readline
n, m, x = map(int, input().split())
arr_h = [[] for _ in range(n + 1)]
arr_l = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    arr_h[a].append(b)
    arr_l[b].append(a)

cnt_l = check(x, arr_h)
cnt_h = check(x, arr_l)
print(cnt_h + 1, n - cnt_l)