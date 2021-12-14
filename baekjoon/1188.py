# 음식 평론가
# https://www.acmicpc.net/problem/1188

import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

input = sys.stdin.readline
n, m = map(int, input().split())
print(m - gcd(n, m))