# 금광

t = int(input())
for i in range(t):
    n, m = map(int, input().split())    
    x = list(map(int, input().split()))
    arr = []
    idx = 0
    for j in range(n):
        arr.append(x[idx:idx + m])
        idx += m
    
    d = [[0] * m for i in range(n)]
    for j in range(n):
        d[j][0] = arr[j][0]
    
    for j in range(1, m):
        for k in range(n):
            case1 = k - 1
            case2 = k
            case3 = k + 1
            if case1 < 0:
                case1 = 0
            if case3 >= n:
                case3 = k
            d[k][j] = arr[k][j] + max(d[case1][j - 1], d[case2][j - 1], d[case3][j - 1])
    
    ans = 0
    for j in range(n):
        if d[j][m - 1] > ans:
            ans = d[j][m - 1]

    print(ans)



# 풀이

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)