# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# r1 x
# https://www.acmicpc.net/problem/2422

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = True
    arr[j - 1][i - 1] = True

cnt = 0

for i in combinations(range(n), 3):
    a, b, c = i
    if arr[a][b] or arr[a][c] or arr[b][c]:
        continue
    cnt += 1
print(cnt)