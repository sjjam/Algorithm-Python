# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def div(num):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            div_list.append(i)
    return div_list

def solution(brown, yellow):
    answer = []
    all_t = brown + yellow
    div_list = div(all_t)
    
    for row in div_list:
        col = all_t // row
        b = row * 2 + (col - 2) * 2
        y = all_t - b

        if b == brown and y == yellow and row >= col:
            answer.append(row)
            answer.append(col)
            break

    return answer