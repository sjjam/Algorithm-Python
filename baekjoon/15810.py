# 풍선 공장
# https://www.acmicpc.net/problem/15810

n, m = map(int, input().split())
a = list(map(int, input().split()))
min_a = min(a) * m
start = 0
end = min_a
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in a:
        cnt += mid // i
    
    if cnt < m:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)



# 풀이 2
# 우선순위큐 사용
# https://moons-memo.tistory.com/168

import sys
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
q = []

for i in a:
    heapq.heappush(q, [i, i])
cnt = 0
timeSum = 0

while True:
    if cnt == m:
        break
    s, t = heapq.heappop(q)
    cnt += 1
    timeSum = s
    heapq.heappush(q, [s + t, t])

print(timeSum)