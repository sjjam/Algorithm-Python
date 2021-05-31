# 디지털시계
# https://www.acmicpc.net/problem/1942

for _ in range(3):
    start, end = input().split(' ')
    h, m, s = map(int, start.split(':'))
    end = list(map(int, end.split(':')))
    time = []

    while True:
        if s == 60:
            s = 0
            m += 1
        
        if m == 60:
            m = 0
            h += 1
        
        if h == 24:
            h = 0

        now = ''
        if h != 0:
            now += str(h)
        if not (now == '' and m == 0):
            if m < 10:
                now += '0'
            now += str(m)
        if s < 10:
            now += '0'
        now += str(s)
        
        if now[0] == '0':
            now = int(now[1:])
        else:
            now = int(now)
        time.append(now)

        if h == end[0] and m == end[1] and s == end[2]:
            break
        
        s += 1

    result = 0
    for i in time:
        if i % 3 == 0:
            result += 1
    print(result)