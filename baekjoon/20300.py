# 서강근육맨
# https://www.acmicpc.net/problem/20300

n = int(input())
data = list(map(int, input().split()))
data.sort()
sumValue = 0
m = 0

if n % 2 != 0:
    m = data.pop()

while len(data) > 0:
    sumValue = data[0] + data[-1]
    data.pop(0)
    data.pop()
    if m < sumValue:
        m = sumValue

print(m)