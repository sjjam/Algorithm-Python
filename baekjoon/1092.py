# 배
# https://www.acmicpc.net/problem/1092

n = int(input())
limit = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
ans = 0

limit.sort(reverse=True)
box.sort(reverse=True)

if box[0] > limit[0]:
    ans = -1
else:
    while True:
        if len(box) == 0:
            break
        for i in range(n):
            for j in range(len(box)):
                if limit[i] >= box[j]:
                    del box[j]
                    break
        ans += 1
print(ans)