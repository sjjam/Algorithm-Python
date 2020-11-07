# 효율적인 화폐 구성

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# d = [10001] * (m + 1)
# for i in range(len(arr)):
#     num = 1
#     idx = arr[i]
#     d[idx] = 1
#     while True:
#         if idx > m:
#             break
#         if d[idx - arr[i]] != 0:
#             d[idx] = min(d[idx - arr[i]] + 1, d[idx])
#         idx += 1

# print(d[:m + 1])
# if d[m] == 0:
#     print(-1)
# else:
#     print(d[m])



# 풀이

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])