# 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

from collections import deque
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    store = []
    for i in range(n):
        store.append(list(map(int, input().split())))
    end_x, end_y = map(int, input().split())

    q = deque()
    q.append((x, y))
    visited = []
    check = False

    while q:
        x, y = q.popleft()
        
        if abs(x - end_x) + abs(y - end_y) <= 20 * 50:
            check = True
            break

        for i in store:
            if i not in visited:
                dist = abs(x - i[0]) + abs(y - i[1])
                if dist <= 20 * 50:
                    visited.append(i)
                    q.append(i)
    
    if check:
        print('happy')
    else:
        print('sad')