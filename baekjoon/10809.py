# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

s = input()

for i in range(97, 123):
    now = chr(i)
    if now in s:
        print(s.index(now), end=' ')
    else:
        print(-1, end=' ')