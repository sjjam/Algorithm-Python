# 소수상근수
# https://www.acmicpc.net/problem/9421

import math

n = int(input())
answer = []

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        now = i
        used = []
        while True:
            str_now = list(str(now))
            now = 0
            for j in str_now:
                now += int(j) ** 2
            
            if now in used:
                break
            if now == 1:
                answer.append(i)
                break
            used.append(now)

for i in answer:
    print(i)