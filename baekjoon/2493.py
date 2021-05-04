# 탑
# https://www.acmicpc.net/problem/2493

n = int(input())
data = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):
    while stack:
        idx, length = stack[-1]
        if data[i] < length:
            ans.append(idx + 1)
            break
        stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, data[i]])

print(" ".join(map(str, ans)))