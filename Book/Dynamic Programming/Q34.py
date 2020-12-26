# 병사 배치하기
# https://www.acmicpc.net/problem/18353




# 풀이

n = int(input())
array = list(map(int, input().split()))
array.reverse()
print(array)
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(n - max(dp))