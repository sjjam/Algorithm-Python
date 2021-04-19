# 다이얼
# https://www.acmicpc.net/problem/5622

data = input()
idx = 2
ans = 0
dic = {}

string = 'A'
while idx < 10:
    now_list = []
    now_list.append(string)
    if idx == 7 or idx == 9:
        for i in range(3):
            string = chr(ord(string) + 1)
            now_list.append(string)
    else:
        for i in range(2):
            string = chr(ord(string) + 1)
            now_list.append(string)
    string = chr(ord(string) + 1)
    dic[idx] = now_list
    idx += 1

for i in data:
    for j in dic.keys():
        if i in dic[j]:
            ans += (j - 1) + 2

print(ans)



data = list(input())
a = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
ans = 0

for ch in data:
    idx = ord(ch) - ord('A')
    ans += a[idx]
print(ans)