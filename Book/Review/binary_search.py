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

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()

# start = 0
# end = arr[n - 1]
# ans = 0
# while start <= end:
#     mid = (start + end) // 2

#     result = 0
#     for i in arr:
#         if mid < i:
#             result += i - mid

#     if result < m:
#         end = mid - 1
#     else:
#         ans = mid
#         start = mid + 1

# print(ans)



# 정렬된 배열에서 특정 수의 개수 구하기
# r1

# n, x = map(int, input().split())
# data = list(map(int, input().split()))

# def binary_search_left(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
#             return mid
#         elif arr[mid] >= target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# def binary_search_right(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if (mid == n - 1 or target < arr[mid + 1]) and arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# if binary_search_left(data, x, 0, n - 1) == None:
#     print(-1)
# else:
#     print(binary_search_right(data, x, 0, n - 1) - binary_search_left(data, x, 0, n - 1) + 1)



# 고정점 찾기
# r1

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
arr = list(map(int, input().split()))

ans = binary_search(arr, 0, n - 1)
if ans == None:
    print(-1)
else:
    print(ans)