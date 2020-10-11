# 왕실의 나이트

now = input()

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']

c, r = list(now)
idxc = 0
idxr = 0

if c in col:
    idxc = col.index(c)
if r in row:
    idxr = row.index(r)

dx = [-2, -2, 1, -1, 2, 2, -1, 1]
dy = [-1, 1, -2, -2, -1, 1, 2, 2]

ans = 0

for i in range(8):
    nx = idxr + dx[i]
    ny = idxc + dy[i]
    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        ans += 1

print(ans)


# 풀이

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)