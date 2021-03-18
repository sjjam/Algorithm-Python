# 도둑질
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0
    d = [0] * len(money)
    d[0] = money[0]
    for i in range(1, len(money) - 1):
        d[i] = max(d[i - 2] + money[i], d[i - 1])
    result = max(d)
    
    d = [0] * len(money)
    d[1] = money[1]
    for i in range(2, len(money)):
        d[i] = max(d[i - 2] + money[i], d[i - 1])
    answer = max(result, max(d))
    return answer