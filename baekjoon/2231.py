# 분해합
# https://www.acmicpc.net/problem/2231

n = int(input())
ans = 0

for i in range(n):
    str_n = str(i)
    x = 0

    for j in range(len(str_n)):
        x += int(str_n[j])

    if i + x == n:
        ans = i
        break

print(ans)