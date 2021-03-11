# 빗물
# https://www.acmicpc.net/problem/14719

h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, w - 1):
    left = block[i]
    for j in range(i - 1, -1, -1):
        if block[j] > left:
            left = block[j]
    right = block[i]
    for j in range(i + 1, w):
        if block[j] > right:
            right = block[j]
    high = min(left, right)
    ans += high - block[i]

print(ans)