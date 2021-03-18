# 디스크 컨트롤러
# r1
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0
    start, now, cnt = -1, 0, 0
    h = []

    while cnt < len(jobs):
        for i in jobs:
            req, time = i
            if start < req <= now:
                heapq.heappush(h, (time, req))

        if len(h) > 0:
            time, req = heapq.heappop(h)
            start = now
            now += time
            answer += now - req
            cnt += 1
        else:
            now += 1
    answer //= len(jobs)
    return answer