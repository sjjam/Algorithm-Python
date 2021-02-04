# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 0

    parent = [0] * n
    for i in range(n):
        parent[i] = i
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_parent(parent, i, j)

    ans_list = set()
    for i in range(n):
        ans_list.add(find_parent(parent, i))
    answer = len(ans_list)

    return answer


# dfs 풀이

def visit(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            visit(i, graph, visited)

def solution(n, computers):
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            answer += 1
        if 0 not in visited:
            break

    return answer