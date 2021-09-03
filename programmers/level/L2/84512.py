# 위클리 5주차
# https://programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = 0
    word_list = ['A', 'E', 'I', 'O', 'U']
    dic = []
    for i in range(1, 6):
        dic += list(product(word_list, repeat=i))
    dic.sort()
    answer = dic.index(tuple(list(word))) + 1
    return answer