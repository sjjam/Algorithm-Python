# 문자열 복사
# https://www.acmicpc.net/problem/2195

from collections import deque

s = input()
p = input()
ans = 0

q = deque()
q.append('')
while q:
    now = q.popleft()
    if now == p:
        break

    for i in range(len(p) - 1, len(now) - 1, -1):
        print(i, p[len(now):i + 1])
        if p[len(now):i + 1] in s:
            ans += 1
            now += p[len(now):i + 1]
            q.append(now)
            break

print(ans)


# 풀이 2
# 참고 : 백준 sketom 풀이

s = input()
p = input()

count = 0
i = 0
while i < len(p):
    count += 1

    result = 0
    maxLength = 0
    index = 0
    while True:
        result = s.find(p[i], result)
        if result == -1:
            break

        tempLength = 0
        tempSIndex = result
        tempPIndex = i
        while s[tempSIndex] == p[tempPIndex]:
            tempLength += 1

            if tempSIndex + 1 == len(s) or tempPIndex + 1 == len(p):
                break

            tempSIndex += 1
            tempPIndex += 1

        if maxLength < tempLength:
            index = tempSIndex
            maxLength = tempLength

        result += tempLength

    i += maxLength

print(count)