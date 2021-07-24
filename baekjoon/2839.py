# 설탕 배달
# https://www.acmicpc.net/problem/2839

n = int(input())
dp = [0] * (5001)
dp[3] = 1
dp[5] = 1

for i in range(6, n + 1):
    if dp[i - 3] != 0:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != 0:
        if dp[i] == 0:
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = min(dp[i - 5] + 1, dp[i])

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])