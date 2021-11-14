# 최대공약수
# https://www.acmicpc.net/problem/2824

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))
a = 1
b = 1

for i in a_list:
    a *= i

for i in b_list:
    b *= i

ans = 0
ans = gcd(a, b)
if len(str(ans)) > 9:
    ans = str(ans)[-9:]
print(ans)