# 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
tri = []

for i in range(n):
    tri.append(list(map(int, input().split())))

d = [[0] * n for i in range(n)]
d[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            tmp = d[i - 1][j] + tri[i][j]
        elif j == i:
            tmp = d[i - 1][j - 1] + tri[i][j]
        else:
            tmp = max(d[i - 1][j - 1], d[i - 1][j]) + tri[i][j]
        d[i][j] = tmp

print(max(d[n - 1]))



# 풀이

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))