# 1이 될 때까지

# n, k = map(int, input().split())
# ans = 0

# while n != 1:
#     if n % k == 0:
#         n /= k
#         ans += 1
#     else:
#         n -= 1
#         ans += 1

# print(ans)

# 풀이1

# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)

# 풀이2

n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)