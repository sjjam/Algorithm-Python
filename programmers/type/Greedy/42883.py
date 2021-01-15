# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    idx = 0
    chk = len(number) - k
    while k != 0 and chk != 0:
        max_n = -1
        pcnt = 0
        cnt = -1
        end = idx + k + 1
        if idx + k + 1 > len(number):
            end = len(number)
        for i in range(idx, end):
            cnt += 1
            if number[i] =='9':
                max_n = int(number[i])
                idx = i + 1
                pcnt = cnt
                break
            if int(number[i]) > max_n:
                max_n = int(number[i])
                idx = i + 1
                pcnt = cnt
        answer += str(max_n)
        chk -= 1
        k -= pcnt
    if chk != 0:
        answer += str(number[idx:])
    print(answer)
    return answer


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

print(solution('4177252841', 4))