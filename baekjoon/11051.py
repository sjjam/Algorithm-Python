# 이항 계수 2
# r1 x
# https://www.acmicpc.net/problem/11051

# https://rh-tn.tistory.com/32

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(0, n + 1):
    for j in range(0, i + 1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k] % 10007)