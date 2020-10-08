# 곱하기 혹은 더하기

s = input()

ints = []
for i in s:
    if i != '0':
        ints.append(int(i))

ints.sort()
ans = ints[0]
for i in range(1, len(ints)):
    if ans == 1:
        ans += ints[i]
    if ints[i] == 1:
        ans += ints[i]
    else:
        ans *= ints[i]
print(ans)


# 풀이

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)