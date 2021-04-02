# N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

def check(i, col):
    global answer
    n = len(col) - 1
    if pormising(i, col):
        if i == n:
            answer += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                check(i + 1, col)

def pormising(i, col):
    # print(i, col)
    for k in range(1, i):
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
    return True

def solution(n):
    global answer
    answer = 0
    col = [0] * (n + 1)
    check(0, col)
    return answer

solution(4)