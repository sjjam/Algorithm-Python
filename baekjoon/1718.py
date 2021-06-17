# 암호
# https://www.acmicpc.net/problem/1718

text = list(input())
key = list(input())

order = []
for i in range(ord('a'), ord('z') + 1):
    order.append(chr(i))

idx = 0
result = ''

for i in text:
    if i != ' ':
        pos = order.index(key[idx])
        now = order.index(i)
        result += order[(now - pos) % len(order) - 1]
    else:
        result += ' '
    idx = (idx + 1) % len(key)
print(result)