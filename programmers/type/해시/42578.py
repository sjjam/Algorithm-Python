# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    keys = dic.keys()
    
    for i in keys:
        answer *= (dic[i] + 1)
    answer -= 1

    return answer