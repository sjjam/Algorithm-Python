# 블록 놀이
# https://www.acmicpc.net/problem/16951

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
h = list(map(int, input().split()))
ans = 1001

for i in range(n):
    cnt = 0
    
    for j in range(n):
        now = k * (j - i) + h[i]
        if now < 1:
            cnt = n
            break
        if now != h[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)