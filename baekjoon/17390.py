# 이건 꼭 풀어야 해!
# https://www.acmicpc.net/problem/17390

import sys

input = sys.stdin.readline
n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

sum_list = [0] * (n + 1)
for i in range(1, n + 1):
	sum_list[i] = sum_list[i - 1] + arr[i - 1]

for _ in range(q):
	l, r = map(int, input().split())
	print(sum_list[r] - sum_list[l - 1])