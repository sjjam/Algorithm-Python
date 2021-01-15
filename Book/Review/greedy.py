# 3-2
# r1

# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))

# arr.sort(reverse=True)
# ans = 0

# cnt = 0
# for i in range(m):
#     if cnt < k:
#         ans += arr[0]
#         cnt += 1
#     elif cnt == k:
#         ans += arr[1]
#         cnt = 0

# print(ans)



# 3-3
# r1

# n, m = map(int, input().split())
# result = []
# for _ in range(n):
#     data = list(map(int, input().split()))
#     result.append(min(data))

# print(max(result))



# 3-4
# r1

# n, k = map(int, input().split())
# ans = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         ans += 1
#     n //= k
#     ans += 1

# while n > 1:
#     n -= 1
#     ans += 1

# print(ans)



# 모험가 길드
# r1

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# ans = 0
# group = []
# for i in data:
#     group.append(i)
#     if i <= len(group):
#         ans += 1
#         group.clear()

# print(ans)



# 곱하기 혹은 더하기
# r1

# s = input()
# result = int(s[0])

# for i in range(1, len(s)):
#     if result <= 1 or int(s[i]) <= 1:
#         result += int(s[i])
#     else:
#         result *= int(s[i])

# print(result)



# 문자열 뒤집기
# r1
# https://www.acmicpc.net/problem/1439

# s = input()
# zero = 0
# one = 0

# if s[0] == '1':
#     zero += 1
# else:
#     one += 1

# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         if s[i + 1] == '1':
#             zero += 1
#         else:
#             one += 1

# print(min(zero, one))



# 만들 수 없는 금액
# r1

# from itertools import combinations

# n = int(input())
# data = list(map(int, input().split()))
# d = [0] * (sum(data) + 1)

# for i in range(1, len(data) + 1):
#     s_list = list(combinations(data, i))
#     for j in s_list:
#         if d[sum(j)] == 0:
#             d[sum(j)] = sum(j)

# for i in range(1, len(d)):
#     if d[i] == 0:
#         print(i)
#         break
'''
'''
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# min_n = 1
# for i in data:
#     if min_n < i:
#         break
#     min_n += i

# print(min_n)


# 볼링공 고르기
# r1

n, m = map(int, input().split())
data = list(map(int, input().split()))

ans = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] != data[j]:
            ans += 1

print(ans)