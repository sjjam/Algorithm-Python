# 저울
# https://www.acmicpc.net/problem/10159

n = int(input())
m = int(input())
INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n + 1)]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    data[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            data[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

for i in range(1, n + 1):
    ans = 0
    for j in range(1, n + 1):
        if data[i][j] == INF and data[j][i] == INF:
            ans += 1
    result.append(ans)

for i in result:
    print(i)