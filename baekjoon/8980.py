# 택배
# r1 x
# https://www.acmicpc.net/problem/8980

# https://steadev.tistory.com/15
# https://jjangsungwon.tistory.com/114

n, c = map(int, input().split())
m = int(input())
data = []

for i in range(m):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x:(x[1], x[0]))
answer = 0  # 최대 박스 수
remain = [c] * (n + 1)  # 각 위치에 남은 공간

for i in range(m):
    temp = c  # c개를 옮길 수 있다고 가정
    for j in range(data[i][0], data[i][1]):
        temp = min(temp, remain[j])
    temp = min(temp, data[i][2])
    for j in range(data[i][0], data[i][1]):
        remain[j] -= temp
    answer += temp

print(answer)