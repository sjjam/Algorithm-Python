# 개업
# r1 x
# https://www.acmicpc.net/problem/13910


# http://wookje.dance/2017/05/31/boj-13910-%EA%B0%9C%EC%97%85/
# python3 시간초과, pypy 통과

n, m = map(int, input().split())
size = list(map(int, input().split()))

dp = [10001] * (n + 1)
dp[0] = 0
check = [False] * 20001
check[0] = True

for i in range(m):
    check[size[i]] = True
    for j in range(i + 1, m):
        check[size[i] + size[j]] = True

for i in range(1, n + 1):
    if not check[i]:
        continue
    for j in range(i, n + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[n] == 10001:
    print(-1)
else:
    print(dp[n])