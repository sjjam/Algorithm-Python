# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

import heapq
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    h = []
    result = []
    for i in range(len(priorities)):
        q.append((priorities[i], i))
        heapq.heappush(h, (-priorities[i], i))

    for i in range(len(h)):
        p, l = heapq.heappop(h)
        result.append((-p, l))

    ans = []
    while q:
        p, l = q.popleft()
        if p >= result[0][0]:
            ans.append((p, l))
            result.pop(0)
        else:
            q.append((p, l))

    for i in range(len(ans)):
        if ans[i][1] == location:
            answer = i + 1
            break

    return answer

solution([2, 1, 4, 5, 3, 2], 2)