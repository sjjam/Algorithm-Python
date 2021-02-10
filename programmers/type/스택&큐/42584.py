# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        now = q.popleft()
        time = 0

        for i in q:
            time += 1
            if i < now:
                break
        answer.append(time)
    return answer