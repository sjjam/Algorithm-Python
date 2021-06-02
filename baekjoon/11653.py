# 소인수분해
# https://www.acmicpc.net/problem/11653

n = int(input())

if n == 1:
    print()
else:
    num = 2
    while num <= n ** 0.5:
        if n % num == 0:
            n //= num
            print(num)
        else:
            num += 1
if n > 1:
    print(n)