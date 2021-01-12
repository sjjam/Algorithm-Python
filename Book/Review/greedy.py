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

n, k = map(int, input().split())
ans = 0

while n >= k:
    while n % k != 0:
        n -= 1
        ans += 1
    n //= k
    ans += 1

while n > 1:
    n -= 1
    ans += 1

print(ans)