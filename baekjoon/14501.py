# 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
answer = 0

dp = [0] * n
for i in range(n):
    if (i + data[i][0] - 1) < n:
        dp[i + data[i][0] - 1] = max(dp[i + data[i][0] - 1], answer + data[i][1])

    if answer < dp[i]:
        answer = dp[i]

print(answer)