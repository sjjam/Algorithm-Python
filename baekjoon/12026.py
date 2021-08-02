# BOJ 거리
# https://www.acmicpc.net/problem/12026

n = int(input())
data = list(input())
dp = [n * n] * n
dp[0] = 0

for i in range(1, n):
    prev = ''
    if data[i] == 'B':
        prev = 'J'
    elif data[i] == 'O':
        prev = 'B'
    else:
        prev = 'O'
    
    for j in range(i):
        if data[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i - j)**2)

if dp[n - 1] == n * n:
    print(-1)
else:
    print(dp[n - 1])