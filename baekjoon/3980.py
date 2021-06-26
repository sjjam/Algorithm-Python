# 선발 명단
# r1 x
# https://www.acmicpc.net/problem/3980

def check(idx, sum_squad):
    global answer
    if idx == 11:
        answer = max(answer, sum_squad)
        return
    
    for i in range(11):
        if squad[i]:
            continue
        if data[idx][i] != 0:
            squad[i] = True
            check(idx + 1, sum_squad + data[idx][i])
            squad[i] = False

for _ in range(int(input())):
    data = []
    for i in range(11):
        data.append(list(map(int, input().split())))
    
    squad = [False] * 11
    answer = 0
    check(0, 0)
    print(answer)