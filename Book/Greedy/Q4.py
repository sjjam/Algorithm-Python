# 만들 수 없는 금액

# n = int(input())
# data = list(map(int, input().split()))

# data.sort()
# result = set()

# sum = 0
# for i in range(len(data)):
#     result.add(data[i])
#     sum += data[i]
#     result.add(sum)
#     sum2 = 0
#     for j in range(i + 1, len(data)):
#         result.add(data[i] + data[j])
#         result.add(sum + data[j])
#         sum2 += data[j]
#         result.add(sum2)

# print(result)
# for i in range(1, len(result) + 1):
#     if i not in result:
#         print(i)
#         break




# 풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)