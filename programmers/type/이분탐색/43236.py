# 징검다리
# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance

    while start <= end:
        target = (start + end) // 2
        cnt = 0

        now = 0
        for i in rocks:
            if i - now < target:
                cnt += 1
            else:
                now = i
        
        if cnt > n:
            end = target - 1
        else:
            answer = target
            start = target + 1

    return answer