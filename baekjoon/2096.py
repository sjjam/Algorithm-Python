# 내려가기
# https://www.acmicpc.net/problem/2096

n = int(input())
maxL = list(map(int, input().split()))
minL = [maxL[0], maxL[1], maxL[2]]
now_max = [0] * 3
now_min = [0] * 3

for i in range(1, n):
    data = list(map(int, input().split()))

    for j in range(3):
        if j == 0:
            now_max[0] = data[0] + max(maxL[0], maxL[1])
            now_min[0] = data[0] + min(minL[0], minL[1])
        elif j == 2:
            now_max[2] = data[2] + max(maxL[1], maxL[2])
            now_min[2] = data[2] + min(minL[1], minL[2])
        else:
            now_max[1] = data[1] + max(maxL)
            now_min[1] = data[1] + min(minL)
    
    maxL = [now_max[0], now_max[1], now_max[2]]
    minL = [now_min[0], now_min[1], now_min[2]]

print(max(maxL), min(minL))