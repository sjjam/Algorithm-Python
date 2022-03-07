# 카드2
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
now = deque()

for i in range(1, n + 1):
    now.append(i)

while True:
    if len(now) == 1:
        print(now[0])
        break
    
    now.popleft()
    left = now.popleft()
    now.append(left)