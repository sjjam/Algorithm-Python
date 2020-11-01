# 떡볶이 떡 만들기

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

start = 0
end = array[n - 1]
while True:
    mid = (start + end) // 2
    sum = 0
    for i in array:
        if i > mid:
            sum += i - mid
    if sum == m:
        break
    elif sum > m:
        start = mid + 1
    else:
        end = mid - 1

print(mid)


# 풀이

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)