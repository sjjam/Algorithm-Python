# NBA 농구
# https://www.acmicpc.net/problem/2852

def plus_zero(num):
    if num == 0:
        return '00'
    if len(str(num)) == 1:
        return '0' + str(num)
    return str(num)

n = int(input())
score_a = 0
score_b = 0
time_a = 0
time_b = 0
win = ''
time = 0
for _ in range(n):
    line = input().split()
    if line[0] == '1':
        score_a += 1
    elif line[0] == '2':
        score_b += 1
    
    now_m, now_s = map(int, line[1].split(":"))
    now_time = now_m * 60 + now_s

    if win == 'a':
        time_a += now_time - time
    elif win == 'b':
        time_b += now_time - time
    
    if score_a > score_b:
        win = 'a'
    elif score_b > score_a:
        win = 'b'
    else:
        win = ''

    time = now_time

if win == 'a':
    time_a += 48 * 60 - time
elif win == 'b':
    time_b += 48 * 60 - time

print(plus_zero(time_a // 60) + ":" + plus_zero(time_a % 60))
print(plus_zero(time_b // 60) + ":" + plus_zero(time_b % 60))