# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

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

def solution(n, costs):
    answer = 0
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    
    costs.sort(key=lambda x: x[2])

    for edge in costs:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer