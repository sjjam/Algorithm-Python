# 두 배열의 합
# r1 x
# https://www.acmicpc.net/problem/2143

# https://hillier.tistory.com/73
# https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9

from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
dic = defaultdict(int)
cnt = 0

for i in range(n):
    for j in range(i, n):
        dic[sum(a[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        cnt += dic[t - sum(b[i:j + 1])]

print(cnt)