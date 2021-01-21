# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            score[0] += 1
        if answers[i] == b[i % len(b)]:
            score[1] += 1
        if answers[i] == c[i % len(c)]:
            score[2] += 1
    
    max_ans = max(score)
    if max_ans == score[0]:
        answer.append(1)
    if max_ans == score[1]:
        answer.append(2)
    if max_ans == score[2]:
        answer.append(3)

    return answer