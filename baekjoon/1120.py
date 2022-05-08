# 문자열
# https://www.acmicpc.net/problem/1120

import sys

input = sys.stdin.readline
a, b = input().split()

if len(a) == len(b):
    dif = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dif += 1
    print(dif)
else:
    dif = len(a)
    for i in range(len(b) - len(a) + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[j + i]:
                cnt += 1
        dif = min(dif, cnt)
    print(dif)