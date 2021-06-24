# 최소, 최대 2
# https://www.acmicpc.net/problem/20053

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print(data[0], data[n - 1])