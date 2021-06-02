# 완전 이진 트리
# https://www.acmicpc.net/problem/9934

def make(data, now):
    mid = len(data) // 2
    tree[now].append(data[mid])
    if len(data) == 1:
        return
    make(data[:mid], now + 1)
    make(data[mid + 1:], now + 1)

k = int(input())
data = list(map(int, input().split()))
tree = [[] for _ in range(k)]
make(data, 0)

for i in tree:
    for j in i:
        print(j, end=' ')
    print()