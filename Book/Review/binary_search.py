# 7-1
# r1

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# a.sort()
# for i in b:
#     result = binary_search(a, i, 0, n - 1)
#     if result == None:
#         print('no', end=' ')
#     else:
#         print('yes', end=' ')



# 7-2
# r1

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = arr[n - 1]
ans = 0
while start <= end:
    mid = (start + end) // 2

    result = 0
    for i in arr:
        if mid < i:
            result += i - mid

    if result < m:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)