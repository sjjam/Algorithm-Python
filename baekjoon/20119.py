# 클레어와 물약
# r1 x
# https://www.acmicpc.net/problem/20119

# https://welog.tistory.com/256

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]
recipe_dict = {}

for _ in range(m):
    data = list(map(int, input().split()))

    if data[-1] not in recipe_dict:
        recipe_dict[data[-1]] = [[data[1:-1], data[0]]]
    else:
        recipe_dict[data[-1]].append([data[1:-1], data[0]])
    
    for i in range(1, len(data) - 1):
        graph[data[i]].add(data[-1])

l = int(input())
l_list = list(map(int, input().split()))
check = [False] * (n + 1)
result = set()

for i in l_list:
    check[i] = True
    result.add(i)

q = deque(l_list)

while q:
    now = q.popleft()

    for i in graph[now]:
        if check[i]:
            continue

        for idx in range(len(recipe_dict[i])):
            recipe, cnt = recipe_dict[i][idx]
            
            if now in recipe:
                recipe.remove(now)
                cnt -= 1
                recipe_dict[i][idx] = [recipe, cnt]

                if cnt == 0:
                    check[i] = True
                    q.append(i)
                    result.add(i)

print(len(result))
result = list(result)
result.sort()
print(*result)