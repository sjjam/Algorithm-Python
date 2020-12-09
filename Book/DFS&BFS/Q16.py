# 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
import copy

n, m = map(int, input().split())
arr = []
void = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
    for j in range(m):
        if l[j] == 0:
            void.append((i, j))

pos = list(combinations(void, 3))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def virus(arr_c, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if arr_c[nx][ny] == 0:
                arr_c[nx][ny] = 2
                virus(arr_c, nx, ny)

ans = 0
for w in pos:
    arr_c = copy.deepcopy(arr)
    for wall in w:
        arr_c[wall[0]][wall[1]] = 1
    
    tmp = 0
    for i in range(n):
        for j in range(m):
            if arr_c[i][j] == 2:
                virus(arr_c, i, j)
    
    for i in range(n):
        for j in range(m):
            if arr_c[i][j] == 0:
                tmp += 1

    if tmp > ans:
        ans = tmp

print(ans)



# 풀이

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)