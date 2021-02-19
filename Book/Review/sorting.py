# 6-1
# r1

# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))

# data.sort(reverse=True)

# for i in data:
#     print(i, end=' ')



# 6-2
# r1

# n = int(input())
# data = []
# for i in range(n):
#     name, age = input().split()
#     data.append((name, int(age)))

# data.sort(key=lambda x:x[1])

# for i in data:
#     print(i[0], end=' ')



# 6-3
# r1

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]

# print(sum(a))



# 국영수
# r1
# https://www.acmicpc.net/problem/10825

# n = int(input())
# data = []
# for i in range(n):
#     name, s1, s2, s3 = input().split()
#     data.append([name, int(s1), int(s2), int(s3)])

# data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

# for i in data:
#     print(i[0])



# 안테나
# r1
# https://www.acmicpc.net/problem/18310

n = int(input())
pos = list(map(int, input().split()))
pos.sort()

ans = pos[(n - 1) // 2]

print(ans)