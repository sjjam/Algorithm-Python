# 특정 거리의 도시 찾기

n, m, k, x = map(int, input().split())
array = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)

