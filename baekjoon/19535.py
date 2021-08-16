# ㄷㄷㄷㅈ
# r1 x
# https://www.acmicpc.net/problem/19535

# https://rhdtka21.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-BOJ-19535-%E3%84%B7%E3%84%B7%E3%84%B7%E3%85%88

import sys
input = sys.stdin.readline

def comb(a, b):
    ans = 1
    for i in range(a - b + 1, a + 1):
        ans *= i
    for j in range(1, b + 1):
        ans //= j
    return ans

n = int(input())
edges = []
degree = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    edges.append([a, b])
    degree[a] += 1
    degree[b] += 1

cnt_d = 0
cnt_g = 0

# ㄷ 개수 계산
for edge in edges:
    temp = (degree[edge[0]] - 1) * (degree[edge[1]] - 1)
    cnt_d += temp

# ㅈ 개수 계산
for i in range(1, n + 1):
    if degree[i] >= 3:
        cnt_g += comb(degree[i], 3)

if cnt_d > 3 * cnt_g:
    print('D')
elif cnt_d < 3 * cnt_g:
    print('G')
else:
    print('DUDUDUNGA')