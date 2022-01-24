# 차이를 최대로
# https://www.acmicpc.net/problem/10819

import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in list(permutations(arr, n)):
    now = 0
    for j in range(len(i) - 1):
        now += abs(i[j] - i[j + 1])
    
    ans = max(ans, now)

print(ans)