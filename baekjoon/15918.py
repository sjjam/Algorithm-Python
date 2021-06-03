# 랭퍼든 수열쟁이야!!
# r1 x
# https://www.acmicpc.net/problem/15918

# https://hillier.tistory.com/106 참고

def dfs(idx):
    global answer
    if idx == 2 * n + 1:
        answer += 1
        return
    if data[idx] != 0:
        dfs(idx + 1)
    else:
        for i in range(1, len(used)):
            if not used[i] and idx + i + 1 < 2 * n + 1 and data[idx + i + 1] == 0:
                used[i] = True
                data[idx] = i
                data[idx + i + 1] = i
                dfs(idx + 1)
                used[i] = False
                data[idx] = 0
                data[idx + i + 1] = 0

n, x, y = map(int, input().split())
data = [0] * (2 * n + 1)
used = [False] * (n + 1)
data[x] = y - x - 1
data[y] = y - x - 1
used[y - x - 1] = True
answer = 0

dfs(1)
print(answer)