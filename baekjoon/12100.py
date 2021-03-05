# 2048 (Easy)
# https://www.acmicpc.net/problem/12100

from itertools import product
import copy

# def move(data, d):
#     if d == 'l':
#         for i in range(n):
#             tmp = []
#             tmp2 = []
#             for j in range(n):
#                 if data[i][j] != 0:
#                     tmp.append(data[i][j])
#             for j in range(len(tmp) - 1):
#                 if tmp[j] == tmp[j + 1]:
#                     tmp2.append(tmp[j] * 2)
#                     tmp[j + 1] = 0
#                 else:
#                     if tmp[j] != 0:
#                         tmp2.append(tmp[j])
#                     if j == len(tmp) - 2 and tmp[j + 1] != 0:
#                         tmp2.append(tmp[j + 1])
#             for j in range(n):
#                 if len(tmp2) != 0:
#                     data[i][j] = tmp2.pop(0)
#                 else:
#                     data[i][j] = 0
#     elif d == 'r':
#         for i in range(n):
#             tmp = []
#             tmp2 = []
#             for j in range(n):
#                 if data[i][j] != 0:
#                     tmp.append(data[i][j])
#             for j in range(len(tmp) - 1, 0, -1):
#                 if tmp[j] == tmp[j - 1]:
#                     tmp2.append(tmp[j] * 2)
#                     tmp[j - 1] = 0
#                 else:
#                     if tmp[j] != 0:
#                         tmp2.append(tmp[j])
#                     if j == 1 and tmp[j - 1] != 0:
#                         tmp2.append(tmp[j - 1])
#             for j in range(n - 1, -1, -1):
#                 if len(tmp2) != 0:
#                     data[i][j] = tmp2.pop(0)
#                 else:
#                     data[i][j] = 0
#     elif d == 'u':
#         for i in range(n):
#             tmp = []
#             tmp2 = []
#             for j in range(n):
#                 if data[j][i] != 0:
#                     tmp.append(data[j][i])
#             for j in range(len(tmp) - 1):
#                 if tmp[j] == tmp[j + 1]:
#                     tmp2.append(tmp[j] * 2)
#                     tmp[j + 1] = 0
#                 else:
#                     if tmp[j] != 0:
#                         tmp2.append(tmp[j])
#                     if j == len(tmp) - 2 and tmp[j + 1] != 0:
#                         tmp2.append(tmp[j + 1])
#             for j in range(n):
#                 if len(tmp2) != 0:
#                     data[j][i] = tmp2.pop(0)
#                 else:
#                     data[j][i] = 0
#     else:
#         for i in range(n):
#             tmp = []
#             tmp2 = []
#             for j in range(n):
#                 if data[j][i] != 0:
#                     tmp.append(data[j][i])
#             for j in range(len(tmp) - 1, 0, -1):
#                 if tmp[j] == tmp[j - 1]:
#                     tmp2.append(tmp[j] * 2)
#                     tmp[j - 1] = 0
#                 else:
#                     if tmp[j] != 0:
#                         tmp2.append(tmp[j])
#                     if j == 1 and tmp[j - 1] != 0:
#                         tmp2.append(tmp[j - 1])
#             for j in range(n - 1, -1, -1):
#                 if len(tmp2) != 0:
#                     data[j][i] = tmp2.pop(0)
#                 else:
#                     data[j][i] = 0
#     return data

def move(arr, d):
    if d == 'u':
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = tmp
                    elif arr[idx][j] == tmp:
                        arr[idx][j] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[idx][j] = tmp
    elif d == 'd':
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = tmp
                    elif arr[idx][j] == tmp:
                        arr[idx][j] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][j] = tmp
    elif d == 'l':
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = tmp
                    elif arr[i][idx] == tmp:
                        arr[i][idx] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = tmp
    else:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = tmp
                    elif arr[i][idx] == tmp:
                        arr[i][idx] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = tmp
    return arr

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
d = ['l', 'r', 'u', 'd']
ans = 0

for i in list(product(d, repeat=5)):
    arr = copy.deepcopy(data)
    for j in i:
        arr = move(arr, j)
    for a in range(n):
        ans = max(ans, max(arr[a]))

print(ans)