# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
# r1 x

def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for i in times:
            cnt += mid // i
            if cnt >= n:
                break
        
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer