# 아이폰 9S
# https://www.acmicpc.net/problem/5883

import sys
import copy

input = sys.stdin.readline
n = int(input())
arr = []
b = []
for _ in range(n):
    data = int(input())
    arr.append(data)
    if data not in b:
        b.append(data)
ans = 0

for i in b:
    arr_copy = copy.deepcopy(arr)
    rm = 0
    for j in arr_copy:
        if j == i:
            rm += 1
    for j in range(rm):
        arr_copy.remove(i)
    
    result = 1
    cnt = 1
    for j in range(len(arr_copy) - 1):
        if arr_copy[j] == arr_copy[j + 1]:
            cnt += 1
            if j == len(arr_copy) - 2:
                result = max(result, cnt)
        else:
            result = max(result, cnt)
            cnt = 1
    
    ans = max(ans, result)

print(ans)