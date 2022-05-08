# K번째 수
# https://www.acmicpc.net/problem/1300

import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
arr = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        arr.append(i * j)

arr.sort()
print(arr)