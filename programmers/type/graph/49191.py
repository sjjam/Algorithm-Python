# 순위
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    wins, loses = {}, {}
    for i in range(1, n + 1):
        wins[i] = set() # i가 이긴 번호들
        loses[i] = set() # i가 진 번호들
    
    for i in range(1, n + 1):
        for j in results:
            if i == j[0]:
                wins[i].add(j[1])
            if i == j[1]:
                loses[i].add(j[0])
        # i를 이긴 번호들은 i가 이긴 번호들도 이기기 때문에 추가
        for j in loses[i]:
            wins[j].update(wins[i])
        # i에게 진 번호들은 i가 진 번호들한테도 지기 때문에 추가
        for j in wins[i]:
            loses[j].update(loses[i])
    
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer



# 플로이드 워셜
def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
    
    for i in results:
        graph[i[0]][i[1]] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    check = [True] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] == INF and graph[j][i] == INF:
                check[i] = False
                break
    
    for i in range(1, n + 1):
        if check[i] == True:
            answer += 1
    return answer