# 이중 우선순위 큐
# X
# https://www.acmicpc.net/problem/7662

import sys
import heapq

input = sys.stdin.readline

def sync(q):
    while q and id[q[0][1]] == 0:
        heapq.heappop(q)

for _ in range(int(input())):
    k = int(input())
    min_q = []
    max_q = []
    id = [0] * 1000000

    for i in range(k):
        operation, num = input().split()
        if operation == 'I':
            heapq.heappush(min_q, (int(num), i))
            heapq.heappush(max_q, (-int(num), i))
            id[i] = 1
        else:
            if num == '-1':
                # 이미 제거한 것들을 sync로 제거
                sync(min_q)
                if min_q:
                    # min_q[0] = 최소값, id를 0으로 초기화하고 제거
                    id[min_q[0][1]] = 0
                    heapq.heappop(min_q)
            else:
                sync(max_q)
                if max_q:
                    id[max_q[0][1]] = 0
                    heapq.heappop(max_q)
        
    sync(max_q)
    sync(min_q)

    if len(min_q) == 0:
        print('EMPTY')
    else:
        print(-max_q[0][0], min_q[0][0])