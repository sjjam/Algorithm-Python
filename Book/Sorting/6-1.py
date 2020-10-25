# 위에서 아래로

n = int(input())
array = []

for i in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)

for i in array:
    print(i, end=' ')


# 풀이

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')