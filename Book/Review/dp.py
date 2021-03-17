# 8-1
# r1

# x = int(input())
# d = [0] * 30001
# d[1] = 0

# for n in range(1, x):
#     if d[n * 5] == 0 or d[n * 5] > d[n] + 1:
#         d[n * 5] = d[n] + 1
#     if d[n * 3] == 0 or d[n * 3] > d[n] + 1:
#         d[n * 3] = d[n] + 1
#     if d[n * 2] == 0 or d[n * 2] > d[n] + 1:
#         d[n * 2] = d[n] + 1
#     if d[n + 1] == 0 or d[n + 1] > d[n] + 1:
#         d[n + 1] = d[n] + 1

# print(d[x])



# x = int(input())
# d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])



# 8-2
# r1 x

# n = int(input())
# food = list(map(int, input().split()))
# d = [0] * 100
# d[0] = food[0]
# d[1] = max(food[0], food[1])

# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + food[i])

# print(d[:n])
# print(d[n - 1])



# 8-3
# r1 x

# n = int(input())
# d = [0] * 1001

# d[1] = 1
# d[2] = 3

# for i in range(3, n + 1):
#     d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# print(d)



# 8-4
# r1

# n, m = map(int, input().split())
# n_list = []
# for i in range(n):
#     n_list.append(int(input()))

# n_list.sort()
# d = [10001] * 10001
# for i in n_list:
#     d[i] = 1

# for i in range(n_list[0], m + 1):
#     for j in n_list:
#         d[i] = min(d[i], d[i - j] + 1)

# if d[m] == 10001:
#     d[m] = -1
# print(d[m])



# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))

# d = [10001] * (m + 1)
# d[0] = 0

# for i in range(n):
#     for j in range(array[i], m + 1):
#         if d[j - array[i]] != 10001:
#             d[j] = min(d[j], d[j - array[i]] + 1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])



# 금광
# r1

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     arr = [[0] * m for _ in range(n)]
#     gold = list(map(int, input().split()))
#     idx = 0
#     for i in range(n):
#         for j in range(m):
#             arr[i][j] = gold[idx]
#             idx += 1

#     for j in range(1, m):
#         for i in range(n):
#             if i == 0:
#                 arr[i][j] += max(arr[i][j - 1], arr[i + 1][j - 1])
#             elif i == n - 1:
#                 arr[i][j] += max(arr[i - 1][j - 1], arr[i][j - 1])
#             else:
#                 arr[i][j] += max(arr[i - 1][j - 1], arr[i][j - 1], arr[i + 1][j - 1])

#     ans = 0
#     for i in range(n):
#         ans = max(ans, arr[i][m - 1])

#     print(ans)



# 정수 삼각형
# r1
# https://www.acmicpc.net/problem/1932

# n = int(input())
# arr = []
# for _ in range(n):
#     line = list(map(int, input().split()))
#     arr.append(line)

# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0:
#             arr[i][j] += arr[i - 1][j]
#         elif j == i:
#             arr[i][j] += arr[i - 1][j - 1]
#         else:
#             arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

# print(max(arr[n - 1]))



# 퇴사
# r1 x
# https://www.acmicpc.net/problem/14501

# n = int(input())
# t = []
# p = []
# dp = [0] * (n + 1)
# max_value = 0

# for _ in range(n):
#     x, y = map(int, input().split())
#     t.append(x)
#     p.append(y)

# for i in range(n - 1, -1, -1):
#     time = t[i] + i

#     if time <= n:
#         dp[i] = max(p[i] + dp[time], max_value)
#         max_value = dp[i]
#     else:
#         dp[i] = max_value

# print(max_value)



# 병사 배치하기
# r1 x
# https://www.acmicpc.net/problem/18353

# n = int(input())
# array = list(map(int, input().split()))
# array.reverse()
# print(array)
# dp = [1] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# print(n - max(dp))



# 못생긴 수
# r1 x

# n = int(input())
# d = [0] * n
# d[0] = 1

# idx2, idx3, idx5 = 0, 0, 0
# res2, res3, res5 = 2, 3, 5

# for i in range(1, n):
#     d[i] = min(res2, res3, res5)
    
#     if d[i] == res2:
#         idx2 += 1
#         res2 = d[idx2] * 2
#     if d[i] == res3:
#         idx3 += 1
#         res3 = d[idx3] * 3
#     if d[i] == res5:
#         idx5 += 1
#         res5 = d[idx5] * 5

# print(d[n - 1])



# 편집 거리
# r1 x

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    print(dp)
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))