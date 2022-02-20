# 더하기 사이클
# https://www.acmicpc.net/problem/1110

n = int(input())
str_n = str(n)
ans = 0

while True:
    ans += 1
    if int(str_n) < 10:
        str_n = str_n[-1] + str(0 + int(str_n))[-1]
    else:
        str_n = str_n[-1] + str(int(str_n[0]) + int(str_n[1]))[-1]

    if int(str_n) == n:
        break

print(ans)