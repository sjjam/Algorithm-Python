# 동굴 탐험
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/67260

# https://deok2kim.tistory.com/48 참고

from collections import deque

def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n)]
    visited = [0] * n
    mustA = {}
    mustB = {}

    for i in order:
        mustA[i[0]] = i[1]
        mustB[i[1]] = i[0]
        if i[0] == 0:
            mustA[0] = -1
        if i[1] == 0:
            return False
    
    for i in path:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append(0)

    while q:
        now = q.popleft()
        visited[now] = 1
        print(now)
        # 먼저 방문해야하는 것이 있어서 visited를 2로 바꾸고 넘어간다
        if now == mustA.get(mustB.get(now)):
            visited[now] = 2
        else:
            for i in graph[now]:
                if visited[i] == 0:
                    q.append(i)

                    if mustA.get(i) != None: # 먼저 방문해야 하는 것이면
                        if visited[mustA[i]] == 2: # 방문했지만 선행방문이 있어서 넘어간 것중에서 선행조건이면
                            q.append(mustA[i])
                            visited[mustA[i]] = 1
                        mustA[i] = -1 # 선행조건이면서 나중에 방문할 것보다 먼저온 상황

    for i in visited:
        if i == 0:
            return False

    return answer