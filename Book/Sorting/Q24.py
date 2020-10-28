# 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
array = list(map(int, input().split()))

array.sort()
mid = array[(n - 1) // 2]
print(mid)


# 풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])