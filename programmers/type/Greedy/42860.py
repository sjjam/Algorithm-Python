# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    tmp = [0] * len(name)
    for i in range(len(name)):
        tmp[i] = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

    idx = 0
    while True:
        answer += tmp[idx]
        tmp[idx] = 0

        if sum(tmp) == 0:
            break

        l, r = 1, 1
        while tmp[idx - l] == 0:
            l += 1
        while tmp[idx + r] == 0:
            r += 1

        answer += min(l, r)
        if l < r:
            idx += -l
        else:
            idx += r
    return answer