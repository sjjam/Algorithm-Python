# 0의 개수
# https://www.acmicpc.net/problem/11170

for _ in range(int(input())):
    n, m = map(int, input().split())
    result = 0

    for i in range(n, m + 1):
        now = str(i)
        if '0' in now:
            result += now.count('0')
    
    print(result)