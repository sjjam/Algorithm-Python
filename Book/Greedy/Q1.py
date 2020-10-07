# 모험가 길드

n = int(input())
gild = list(map(int, input().split()))
ans = 0

gild.sort()

group = []
for i in gild:
    group.append(i)
    print(group)
    if i == len(group):
        ans += 1
        group.clear()

print(ans)


# 풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포한된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹 결성
        result += 1
        count = 0

print(result)