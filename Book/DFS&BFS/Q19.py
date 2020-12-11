# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
p, s, m, d = map(int, input().split())

operator_s = [('p', p), ('s', s), ('m', m), ('d', d)]
operator_n = []

for i in operator_s:
    if i[1] != 0:
        for j in range(i[1]):
            operator_n.append(i[0])

operator = list(permutations(operator_n, n - 1))

result_min = 1e9
result_max = -1e9
for i in operator:
    result = arr[0]
    for j in range(n - 1):
        if i[j] == 'p':
            result += arr[j + 1]
        elif i[j] == 's':
            result -= arr[j + 1]
        elif i[j] == 'm':
            result *= arr[j + 1]
        else:
            if result > 0:
                result = result // arr[j + 1]
            else:
                result = -(abs(result) // arr[j + 1])
    
    if result > result_max:
        result_max = result
    if result < result_min:
        result_min = result

print(result_max)
print(result_min)




# 풀이

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)