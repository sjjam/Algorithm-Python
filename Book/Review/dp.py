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

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d)