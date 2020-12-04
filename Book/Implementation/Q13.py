# 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
arr = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

store = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            store.append((i, j))
        elif arr[i][j] == 1:
            home.append((i, j))

case = list(combinations(store, m))
ans = 10001

for i in case:
    sum_d = [10001] * len(home)
    for j in i:
        for k in range(len(home)):
            now_d = abs(j[0] - home[k][0]) + abs(j[1] - home[k][1])
            if now_d < sum_d[k]:
                sum_d[k] = now_d
    distance = sum(sum_d)
    if distance < ans:
        ans = distance

print(ans)




# 풀이

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)