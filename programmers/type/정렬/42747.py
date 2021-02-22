# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(max(citations), -1, -1):
        m = 0
        for j in citations:
            if j >= i:
                m += 1
        if i <= m:
            answer = i
            break
    print(answer)
    return answer

def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break
    return answer