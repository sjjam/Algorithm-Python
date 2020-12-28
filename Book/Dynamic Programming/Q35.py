# 못생긴 수

n = int(input())
d = [0] * 1001
d[1] = 1
prime = [2, 3, 5]

def check(num):
    su = 2
    so = []

    while su <= num:
        if num % su == 0:
            so.append(su)
            num //= su
        else:
            su += 1
    
    for i in so:
        if i not in prime:
            return False
    
    return True

idx = 2
for i in range(2, 1001):
    if check(i):
        d[idx] = i
        idx += 1

print(d[n])




# 풀이

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])