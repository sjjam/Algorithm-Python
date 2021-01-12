# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    tmp = []
    for i in reserve:
        for j in lost:
            if i == j:
                tmp.append(j)
    
    for i in tmp:
        reserve.remove(i)
        lost.remove(i)
    
    tmp2 = []
    for i in reserve:
        for j in lost:
            if i == j - 1 or i == j + 1:
                lost.remove(j)
                break

    answer = n - len(lost)
    return answer