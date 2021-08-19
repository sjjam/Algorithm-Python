# 롤케이크
# https://www.acmicpc.net/problem/16206

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
# 10으로 나누어 떨어지는 수 우선 처리
a.sort(key=lambda x:(x % 10, x))
ans = 0

for i in range(len(a)):
    if a[i] == 10:
        ans += 1
    elif a[i] > 10:
        if m == 0:
            break
        while True:
            a[i] -= 10
            m -= 1
            ans += 1
            if m == 0 or a[i] <= 10:
                if a[i] == 10:
                    ans += 1
                break

print(ans)