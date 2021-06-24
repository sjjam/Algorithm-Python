# 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
s = []

for i in range(n):
    s.append(input())

for i in range(m):
    if input() in s:
        answer += 1

print(answer)

# s를 set()으로 바꾸면 시간이 많이 줄어들었다
# s가 list일때 3900ms s가 set일떄 140ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
s = set()

for i in range(n):
    s.add(input())

for i in range(m):
    if input() in s:
        answer += 1

print(answer)