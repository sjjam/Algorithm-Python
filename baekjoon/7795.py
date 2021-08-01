# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795

import sys

def binary(b, target):
    start = 0
    end = m - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if b[mid] >= target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    b.sort()

    for i in a:
        ans += binary(b, i) + 1
    print(ans)