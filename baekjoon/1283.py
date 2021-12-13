# 단축키 지정
# https://www.acmicpc.net/problem/1283

import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())

result = []
ans = []

for word in data:
    split = word.split()
    now = ''
    flag = False

    for i in split:
        if i[0].upper() in result or i[0].lower() in result:
            now += i + ' '
        else:
            if flag:
                now += i + ' '
                continue
            now += '[' + i[0] + ']' + i[1:] + ' '
            result.append(i[0])
            flag = True
    
    if flag:
        ans.append(now)
        continue
    else:
        now = ''

    for i in split:
        for j in range(len(i)):
            if i[j].upper() in result or i[j].lower() in result:
                now += i[j]
            else:
                if flag:
                    now += i[j]
                    continue

                flag = True
                now += '[' + i[j] + ']'
                result.append(i[j])
        now += ' '
    ans.append(now)

for i in ans:
    print(i)