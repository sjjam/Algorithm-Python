# 부분합
# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = n + 1

i_sum = 0
end = 0
count = 0

for start in range(n):
    while i_sum < s and end < n:
        i_sum += arr[end]
        end += 1
        count += 1
    if i_sum >= s:
        ans = min(ans, count)
    i_sum -= arr[start]
    count -= 1

if ans == n + 1:
    print(0)
else:
    print(ans)