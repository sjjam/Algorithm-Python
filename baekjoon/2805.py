# 나무 자르기
# https://www.acmicpc.net/problem/2805

from collections import Counter

n, m = map(int, input().split())
data = Counter(map(int, input().split()))
start = 1
end = max(data)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i, cnt in data.items():
        if i > mid:
            total += (i - mid) * cnt
            
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)