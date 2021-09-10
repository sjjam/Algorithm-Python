# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        if i in win_nums:
            same += 1
            win_nums.remove(i)
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer.append(rank[same + zero])
    answer.append(rank[same])

    return answer