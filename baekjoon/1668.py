# 트로피 진열
# https://www.acmicpc.net/problem/1668

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

left = data[0]
cnt_l = 1
cnt_r = 1
right = data[-1]

for i in range(n):
    if data[i] > left:
        left = data[i]
        cnt_l += 1
    if data[n - 1 - i] > right:
        right = data[n - 1 - i]
        cnt_r += 1

print(cnt_l)
print(cnt_r)