# 연속합
# https://www.acmicpc.net/problem/1912

n = int(input())
dp = list(map(int, input().split()))
answer = dp[0]

for i in range(1, n):
    if dp[i - 1] > 0 and dp[i] + dp[i - 1] > 0:
        dp[i] += dp[i - 1]
    
    if answer < dp[i]:
        answer = dp[i]

print(answer)