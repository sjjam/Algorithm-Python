# 생태학
# https://www.acmicpc.net/problem/4358

import sys

input = sys.stdin.readline
arr = dict()
cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    
    cnt += 1
    if tree not in arr:
        arr[tree] = 1
    else:
        arr[tree] += 1

key = list(arr.keys())
key.sort()
for i in key:
    print("%s %.4f" % (i, arr[i]*100/cnt))