# 가장 큰 수
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    str_n = []
    for i in numbers:
        tmp = list(str(i))
        str_n.append(tmp)

    str_n.sort(key=lambda x:x*3, reverse=True)
    print(str_n)
    for i in str_n:
        for j in i:
            answer += j

    return str(int(answer))