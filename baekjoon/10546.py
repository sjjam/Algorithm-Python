# 배부른 마라토너
# https://www.acmicpc.net/problem/10546

import sys
input = sys.stdin.readline

n = int(input())
p = dict()
for _ in range(n):
    now = input().rstrip()
    if now not in p:
        p[now] = 1
    else:
        p[now] += 1

for _ in range(n - 1):
    now = input().rstrip()
    if p[now] == 1:
        p.pop(now)
    elif p[now] >= 2:
        p[now] -= 1

print(list(p.keys())[0])