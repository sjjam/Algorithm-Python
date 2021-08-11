# 복권
# https://www.acmicpc.net/problem/1359

from itertools import combinations

n, m, k = map(int, input().split())
p = len(list(combinations(range(n), m)))
result = 0
while m >= k:
    if n - m < m - k:
        k += 1
    c = len(list(combinations(range(m), k))) * len(list(combinations(range(n - m), m - k)))
    result += c / p
    k += 1

print('%.16f' % result)