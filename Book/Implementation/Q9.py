# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 0
    length = len(s) // 2
    
    result = s
    for i in range(1, length + 1):
        tmp = ""
        same = 1
        for j in range(0, len(s), i):
            if s[j:j + i] == s[j + i:j + i + i]:
                same += 1
            else:
                if same != 1:
                    tmp += str(same) + s[j:j + i]
                else:
                    tmp += s[j:j + i]
                same = 1
        print(tmp)
        if len(tmp) < len(result):
            result = tmp
    answer = len(result)
    print(result, answer)
    return answer

solution("xababcdcdababcdcd")





# 풀이

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

print(solution("ababcdcdababcdcd"))