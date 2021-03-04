# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

def push(arr, x, y, now):
    arr[x][y] = now
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    for i in range(3):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= len(arr) or ny >= len(arr[x]) or nx < 0:
                break

            if arr[nx][ny] != 0:
                if i == 0:
                    nx -= 1
                elif i == 1:
                    ny -= 1
                break
            x = nx
            y = ny
            now += 1
            arr[nx][ny] = now
    now += 1
    return now
    
    # while x < len(arr) - 1:
    #     x += 1
    #     if arr[x][y] != 0:
    #         x -= 1
    #         break
    #     now += 1
    #     arr[x][y] = now
    
    # while y < len(arr) - 1:
    #     y += 1
    #     if arr[x][y] != 0:
    #         y -= 1
    #         break
    #     now += 1
    #     arr[x][y] = now
    
    # while x > 0:
    #     x -= 1
    #     y -= 1
    #     now += 1
    #     if arr[x][y] != 0:
    #         break
    #     arr[x][y] = now
    
    # return now

def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n + 1)]
    
    now = 1
    for i in range(n):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                now = push(arr, i, j, now)
            answer.append(arr[i][j])

    return answer