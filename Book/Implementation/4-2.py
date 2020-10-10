# 시각

n = int(input())

time = ''
h = 0
m = 0
s = 0
cnt = 0

while True:
    time = ''
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    time += str(h) + ':' + str(m) + ':' + str(s)
    if '3' in time:
        cnt += 1
    if time == str(n) + ':59:59':
        break
print(cnt)


# 풀이

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)