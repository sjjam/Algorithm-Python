# 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    
    for q in queries:
        x1, y1, x2, y2 = q
        t = arr[x1 - 1][y1 - 1]
        min_i = t
        
        for i in range(x1 - 1, x2 - 1):
            arr[i][y1 - 1] = arr[i + 1][y1 - 1]
            min_i = min(min_i, arr[i][y1 - 1])
        
        for i in range(y1 - 1, y2 - 1):
            arr[x2 - 1][i] = arr[x2 - 1][i + 1]
            min_i = min(min_i, arr[x2 - 1][i])
        
        for i in range(x2 - 1, x1 - 1, -1):
            arr[i][y2 - 1] = arr[i - 1][y2 - 1]
            min_i = min(min_i, arr[i][y2 - 1])
        
        for i in range(y2 - 1, y1 - 1, -1):
            arr[x1 - 1][i] = arr[x1 - 1][i - 1]
            min_i = min(min_i, arr[x1 - 1][i])
        
        arr[x1 - 1][y1] = t
        answer.append(min_i)
    
    return answer