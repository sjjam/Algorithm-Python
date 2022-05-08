# 괄호의 값
# r1 x
# https://www.acmicpc.net/problem/2504

# https://hongcoding.tistory.com/114

import sys

input = sys.stdin.readline
data = input()
stack = []
score = 1
ans = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
        score *= 2
    elif data[i] == '[':
        stack.append(data[i])
        score *= 3
    elif data[i] == ')':
        if len(stack) == 0 or stack[-1] == '[':
            ans = 0
            break
        if data[i - 1] == '(':
            ans += score
        stack.pop()
        score //= 2
    elif data[i] == ']':
        if len(stack) == 0 or stack[-1] == '(':
            ans = 0
            break
        if data[i - 1] == '[':
            ans += score
        stack.pop()
        score //= 3

if stack:
    print(0)
else:
    print(ans)