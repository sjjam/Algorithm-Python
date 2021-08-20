# 영우는 사기꾼?
# https://www.acmicpc.net/problem/14676

import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
data = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    indegree[y] += 1

result = [0] * (n + 1)
ans = 'King-God-Emperor'
for _ in range(k):
    a, b = map(int, input().split())
    if a == 1:
        if indegree[b] == 0:
            result[b] += 1
            if result[b] == 1:
                for i in data[b]:
                    indegree[i] -= 1
        else:
            ans = 'Lier!'
            break
    else:
        if result[b] == 0:
            ans = 'Lier!'
            break
        else:
            result[b] -= 1
            if result[b] == 0:
                for i in data[b]:
                    indegree[i] += 1

print(ans)