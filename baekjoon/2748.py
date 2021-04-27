# 피보나치 수 2
# https://www.acmicpc.net/problem/2748

n = int(input())
d = [0] * 91
d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i - 2] + d[i - 1]

print(d[n])