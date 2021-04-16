# 성냥개비
# r1 x
# https://www.acmicpc.net/problem/3687

# http://blog.devjoshua.me/2019/11/30/boj-3687/ 참고

import sys

for tc in range(int(input())):
    n = int(input())
    d = [sys.maxsize] * 101
    d[2] = 1
    d[3] = 7
    d[4] = 4
    d[5] = 2
    d[6] = 6
    d[7] = 8

    num = ['1', '7', '4', '2', '0', '8']

    for i in range(8, 101):
        for j in range(2, 8):
            now = str(d[i - j]) + num[j - 2]
            d[i] = min(d[i], int(now))

    min_n = d[n]

    max_n = (n // 2 - 1) * '1'
    max_n = str(d[n - 2 * (n // 2 - 1)]) + max_n
    print(min_n, max_n)