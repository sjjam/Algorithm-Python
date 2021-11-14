# Coins
# https://www.acmicpc.net/problem/3067

# https://velog.io/@uoayop/BOJ-3067-CoinsPython

for _ in range(int(input())):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(n_list[i], m + 1):
            dp[j] += dp[j - n_list[i]]
    
    print(dp[m])