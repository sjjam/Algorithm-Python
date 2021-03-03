# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    
    result = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        if a >= K:
            break
        b = heapq.heappop(h)
        
        result = a + (b * 2)
        heapq.heappush(h, result)
        answer += 1

    if result < K:
        answer = -1
    return answer