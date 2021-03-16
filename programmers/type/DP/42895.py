# N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0
    if N == number:
        return 1
    s = [set() for x in range(8)]
    for i in range(len(s)):
        s[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    if answer > 8 or answer == 0:
        answer = -1

    return answer