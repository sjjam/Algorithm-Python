# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

ans = count_by_range(array, x, x)
if ans == 0:
    ans = -1

print(ans)


# 풀이 1

def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n - 1)
    if a == None:
        return 0

    b = last(array, x, 0, n - 1)
    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)



# 풀이 2(bisect 라이브러리 활용)

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)