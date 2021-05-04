# 오큰수
# r1 x
# https://www.acmicpc.net/problem/17298

n = int(input())
data = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        answer[stack[-1]] = data[i]
        stack.pop()
    stack.append(i)

for i in answer:
    print(i, end=' ')