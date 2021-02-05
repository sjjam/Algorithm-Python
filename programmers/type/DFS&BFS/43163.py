# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)

    while q:
        now, ans = q.popleft()
        if now == target:
            begin = target
            return ans
        for idx in range(len(words)):
            cnt = 0
            for i in range(len(target)):
                if words[idx][i] == now[i]:
                    cnt += 1
            if cnt == len(target) - 1 and visited[idx] == False:
                ans += 1
                q.append((words[idx], ans))
                visited[idx] = True
    if begin != target:
        ans = 0
    return ans

def solution(begin, target, words):
    answer = 0
    answer = bfs(begin, target, words)
    return answer


# dict 활용 풀이

from collections import deque

def bfs(begin, target, words, dic):
    q = deque()
    q.append(begin)

    while q:
        now = q.popleft()
        if now == target:
            break

        for word in words:
            cnt = 0
            for i in range(len(target)):
                if word[i] == now[i]:
                    cnt += 1
            if cnt == len(target) - 1 and dic[word] == 0:
                dic[word] = dic[now] + 1
                q.append(word)
    
    return dic

def solution(begin, target, words):
    answer = 0
    dic = dict()
    dic[begin] = 0
    for i in words:
        dic[i] = 0

    ans = bfs(begin, target, words, dic)
    if target not in dic or dic[target] == 0:
        answer = 0
    else:
        answer = dic[target]
    return answer