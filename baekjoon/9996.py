# 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996

import sys

input = sys.stdin.readline
n = int(input())
pattern = input()
f, e = pattern.split('*')
arr = []

for _ in range(n):
    word = input()
    
    if f == word[:len(f)]:
        word = word[len(f):]
    else:
        print('NE')
        continue

    if e == word[-len(e):]:
        print('DA')
    else:
        print('NE')