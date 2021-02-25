# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = {}

    for i in range(len(plays)):
        if genres[i] not in dic:
            dic[genres[i]] = [(i, plays[i])]
        else:
            dic[genres[i]].append((i, plays[i]))
    
    keys = dic.keys()
    gen_s = []

    for i in keys:
        cnt = 0
        dic[i].sort(key=lambda x:-x[1])
        for j in dic[i]:
            cnt += j[1]
        gen_s.append((cnt, i))
    gen_s.sort(reverse=True)

    for i in gen_s:
        cnt = 0
        for j in dic[i[1]]:
            answer.append(j[0])
            cnt += 1
            if cnt == 2:
                break
    
    return answer