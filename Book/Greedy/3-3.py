# 숫자 카드 게임

n, m = map(int, input().split())
card = [[0]* m for i in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        card[i][j] = x[j]

max = 0
for i in card:
    i.sort()
    if i[0] > max:
        max = i[0]

print(max)


# 풀이1 min() 함수를 이용

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 풀이2 2중 반복문 구조를 이용

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)