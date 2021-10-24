# 2차원 배열의 합
# https://www.acmicpc.net/problem/2167

# https://ywtechit.tistory.com/102

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())
data = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        data[i][j] = arr[i - 1][j - 1] + data[i - 1][j] + data[i][j - 1] - data[i - 1][j - 1]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(data[x][y] - data[i - 1][y] - data[x][j - 1] + data[i - 1][j - 1])