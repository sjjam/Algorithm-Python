# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

string = input()
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
front = ['c', 'd', 'l', 'n', 's', 'z']
idx = 0
ans = 0

while idx < len(string):
    now = string[idx]
    ans += 1
    if now in front:
        for i in range(1, 4):
            if idx + i < len(string):
                now += string[idx + i]
                if now in change:
                    idx += i
                    break
    idx += 1

print(ans)



string = input()
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in change:
    string = string.replace(i, "a")
print(len(string))