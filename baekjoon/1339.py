# 단어 수학
# https://www.acmicpc.net/problem/1339

# https://yoonsang-it.tistory.com/41

n = int(input())
words = []
for _ in range(n):
    words.append(input())

used = dict()
for word in words:
    k = len(word) - 1
    for idx in word:
        if idx in used:
            used[idx] += pow(10, k)
        else:
            used[idx] = pow(10, k)
        k -= 1

change = []
for i in used.values():
    change.append(i)
change.sort(reverse=True)

result = 0
now = 9
for i in change:
    result += i * now
    now -= 1
print(result)