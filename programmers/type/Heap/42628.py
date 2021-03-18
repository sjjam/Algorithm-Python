# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    answer = [0, 0]
    maxH = []
    minH = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(maxH, -int(i[2:]))
            heapq.heappush(minH, int(i[2:]))
        else:
            if len(maxH) > 0:
                if i == 'D -1':
                    minNum = heapq.heappop(minH)
                    maxH.remove(-minNum)
                else:
                    maxNum = -heapq.heappop(maxH)
                    minH.remove(maxNum)

    if len(maxH) > 0:
        answer[1] = heapq.heappop(minH)
        answer[0] = -heapq.heappop(maxH)

    return answer



import heapq

def solution(operations):
    answer = [0, 0]

    h = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(h, int(i[2:]))
        else:
            if len(h) > 0:
                if i == 'D -1':
                    heapq.heappop(h)
                else:
                    h.remove(heapq.nlargest(1, h)[0])
    
    if len(h) > 0:
        answer[0] = heapq.nlargest(1, h)[0]
        answer[1] = heapq.heappop(h)
    
    return answer