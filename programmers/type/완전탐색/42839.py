# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import permutations

def check(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    data = list(numbers)
    d = []
    for i in range(1, len(numbers) + 1):
        result = list(permutations(data, i))
        for j in result:
            tmp = ''
            for k in j:
                tmp += k
            if int(tmp) not in d:
                d.append(int(tmp))
                if check(int(tmp)):
                    answer += 1
    
    print(answer)
    return answer

solution('011')