# 큰 수의 법칙

n, m, k = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
cnt = 0

array.sort(reverse=True)

idx = 0
while True:
    kcnt = 0
    while True:
        ans += array[idx]
        kcnt += 1
        cnt += 1
        if kcnt == k:
            break
        if cnt == m:
            break
        if idx == 1:
            break

    if idx == 0:
        idx = 1
    else:
        idx = 0
    if cnt == m:
        break

print(ans)


# 풀이1

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 풀이2

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k + 1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)