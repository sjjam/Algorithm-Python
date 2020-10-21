# 문자열 재정렬

n = input()

length = len(n)
alpha = []
num = 0
for i in range(length):
    if n[i].isalpha():
        alpha.append(n[i])
    else:
        num += int(n[i])

alpha.sort()

ans = ''
for i in alpha:
    ans += i
if num != 0:
    ans += str(num)
print(ans)


# 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))