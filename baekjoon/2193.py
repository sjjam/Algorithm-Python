# 이친수
# https://www.acmicpc.net/problem/2193

n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    # i - 1에 0 추가, i - 2에 01 추가
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])