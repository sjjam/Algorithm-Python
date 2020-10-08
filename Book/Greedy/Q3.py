# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

s = input()

zero = '0'
nzero = '1'
ans = 0

zl = []
nzl = []
for i in range(len(s)):
    if zero == s[i]:
        zl.append(i)
    else:
        nzl.append(i)

zcnt = 0
nzcnt = 0

for i in range(len(zl) - 1):
    if zl[i] + 1 == zl[i + 1]:
        zcnt += 1

for i in range(len(nzl) - 1):
    if nzl[i] + 1 == nzl[i + 1]:
        nzcnt += 1

if len(zl) - zcnt > len(nzl) - nzcnt:
    ans = len(nzl) - nzcnt
else:
    ans = len(zl) - zcnt

print(ans)

# 풀이

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))