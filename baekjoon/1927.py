# 최소 힙
# https://www.acmicpc.net/problem/1927

import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
    now = int(input())
    if now == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, now)