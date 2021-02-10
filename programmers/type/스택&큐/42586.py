# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    w = []
    for i in range(len(progresses)):
        w.append((progresses[i], speeds[i]))
    
    q = deque(w)

    while q:
        now, speed = q.popleft()
        day = math.ceil((100 - now) / speed)
        rel = 1
        cnt = 0
        # while now < 100:
        #     day += 1
        #     now += speed

        for n, s in q:
            n = n + s * day
            if n >= 100:
                cnt += 1
                rel += 1
            else:
                break
        for i in range(cnt):
            q.popleft()
        answer.append(rel)

    return answer