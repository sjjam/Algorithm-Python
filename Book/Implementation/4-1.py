# 상하좌우

n = int(input())
plan = list(map(str, input().split()))

x = 1
y = 1

for i in range(len(plan)):
    nx = x
    ny = y
    if plan[i] == 'L':
        ny = y - 1
    elif plan[i] == 'R':
        ny = y + 1
    elif plan[i] == 'U':
        nx = x - 1
    elif plan[i] == 'D':
        nx = x + 1
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
        x = nx
        y = ny
print(x, y)


# 풀이

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)