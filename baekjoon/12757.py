# 전설의 JBNU
# https://www.acmicpc.net/problem/12757

from bisect import bisect_left
import sys

input = sys.stdin.readline

def distance(keys, key):
    idx = bisect_left(keys, key)
    if idx == 0:
        if abs(key - keys[idx]) <= k:
            return keys[idx]
    elif idx == len(keys):
        if abs(key - keys[idx - 1]) <= k:
            return keys[idx - 1]
    else:
        if abs(key - keys[idx - 1]) < abs(key - keys[idx]):
            if abs(key - keys[idx - 1]) <= k:
                return keys[idx - 1]
        elif abs(key - keys[idx - 1]) > abs(key - keys[idx]):
            if abs(key - keys[idx]) <= k:
                return keys[idx]
        else:
            if abs(key - keys[idx - 1]) <= k and abs(key - keys[idx]) <= k:
                return '?'
    return -1

n, m, k = map(int, input().split())
data = dict()
keys = []
for _ in range(n):
    key, val = map(int, input().split())
    data[key] = val
    keys.insert(bisect_left(keys, key), key)

for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 1:
        keys.insert(bisect_left(keys, line[1]), line[1])
        data[line[1]] = line[2]
    elif line[0] == 2:
        dist = distance(keys, line[1])
        if dist != -1:
            data[dist] = line[2]
    else:
        dist = distance(keys, line[1])
        if dist == -1:
            print(-1)
        elif dist == '?':
            print('?')
        else:
            print(data[dist])