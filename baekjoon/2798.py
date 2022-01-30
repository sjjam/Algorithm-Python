# 블랙잭
# https://www.acmicpc.net/problem/2798

from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0

for i in list(combinations(card, 3)):
    now = sum(i)
    if now <= m and now > ans:
        ans = now

print(ans)