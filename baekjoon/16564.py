# 히오스 프로게이머
# https://www.acmicpc.net/problem/16564

n, k = map(int, input().split())
lev = []
for _ in  range(n):
    lev.append(int(input()))

lev.sort()
start = lev[0]
end = lev[n - 1]
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = k
    for i in range(n):
        if mid > lev[i]:
            cnt -= mid - lev[i]
        else:
            break
    
    if cnt < 0:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)