# 나눌 수 있는 부분 수열
# r1 x
# https://www.acmicpc.net/problem/3673

# https://devlibrary00108.tistory.com/406

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    m = [0] * 1000000
    m[0] = 1

    now = 0
    for i in range(len(arr)):
        now += arr[i]
        m[now % d] += 1

    ans = 0
    for i in range(d):
        ans += m[i] * (m[i] - 1) // 2
    print(ans)