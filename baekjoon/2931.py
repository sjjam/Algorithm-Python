# 접미사 배열
# https://www.acmicpc.net/problem/11656

answer = []
data = input()

for i in range(len(data)):
    answer.append(data[i:])
answer.sort()

for i in answer:
    print(i)