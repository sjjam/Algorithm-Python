# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    cnt = 0
    idx = 0
    people.sort()
    for i in range(len(people) - 1, -1, -1):
        if i <= idx:
            break
        if people[i] + people[idx] <= limit:
            cnt += 1
            idx += 1
    answer = len(people) - cnt
    return answer