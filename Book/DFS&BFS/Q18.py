# 괄호 변환

p = input()
answer = ''
def dfs(p):
    left = 0
    right = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1
        if left != 0 and left == right:
            u = p[:(i + 1)]
            v = p[(i + 1):]
            break
    if len(u) != 0:
        if u[0] == '(':
            u += dfs(v)
            return u
        else:
            tmp = '('
            tmp += dfs(v)
            tmp += ')'
            tmp2 = ''
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    tmp2 += ')'
                else:
                    tmp2 += '('
            tmp += tmp2
            return tmp
    return u

if len(p) == 0:
    answer = ''
else:
    answer += dfs(p)

print(answer)


# 풀이

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

p = input()
print(solution(p))