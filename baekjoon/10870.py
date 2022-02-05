# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

n = int(input())
arr = [0] * 21
arr[0] = 0
arr[1] = 1

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[n])