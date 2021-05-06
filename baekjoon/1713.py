# 후보 추천하기
# https://www.acmicpc.net/problem/1713

n = int(input())
count = int(input())
order = list(map(int, input().split()))
candidate = [[0, 0, 0]] * n

for i in order:
    change = True
    for j in candidate:
        if i == j[0]:
            j[1] += 1
            change = False
        j[2] += 1
    
    if change:
        candidate.sort(key=lambda x:(x[1], -x[2]))
        candidate.pop(0)
        candidate.append([i, 1, 0])

candidate.sort()
for i in candidate:
    print(i[0], end=' ')



n = int(input())
count = int(input())
order = list(map(int, input().split()))
candidate = [0] * n
score = [0] * n

for i in order:
    if i in candidate:
        for j in range(n):
            if candidate[j] == i:
                score[j] += 1
    else:
        min_cnt = min(score)
        for j in range(n):
            if score[j] == min_cnt:
                candidate.pop(j)
                score.pop(j)
                break
        candidate.append(i)
        score.append(1)

candidate.sort()
for i in candidate:
    print(i, end=' ')