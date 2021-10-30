# 가장 큰 정사각형
# r1 x
# https://www.acmicpc.net/problem/1915


# https://velog.io/@sangjin98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1915%EB%B2%88-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))
ans = 0

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and arr[i][j] == 1:
            arr[i][j] += min(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1])
        ans = max(ans, arr[i][j])

print(ans * ans)