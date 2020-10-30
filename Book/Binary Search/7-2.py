# 떡볶이 떡 만들기

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            return mid
        else:
            start = mid + 1
    return None

for i in array:
    