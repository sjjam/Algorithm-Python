# 이진 검색 트리
# r1 x
# https://www.acmicpc.net/problem/5639

def postorder(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if data[start] < data[i]:
            division = i
            break
    
    postorder(start + 1, division - 1) # 분할 왼쪽
    postorder(division, end) # 분할 오른쪽
    print(data[start])

import sys
sys.setrecursionlimit(10**9)

data = []
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:
        break
    data.append(num)
    count += 1

postorder(0, len(data) - 1)