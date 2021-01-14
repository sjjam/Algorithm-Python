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

s = input()
zero = 0
one = 0

if s[0] == '1':
    zero += 1
else:
    one += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            zero += 1
        else:
            one += 1

print(min(zero, one))