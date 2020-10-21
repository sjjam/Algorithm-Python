# 럭키 스트레이트

n = int(input())

strn = str(n)
mid = len(str(n))//2
left = strn[:mid]
right = strn[mid:]

sumL = 0
sumR = 0

for i in range(mid):
    sumL += int(left[i])
    sumR += int(right[i])

ans = ''
if sumL == sumR:
    ans = 'LUCKY'
else:
    ans = 'READY'

print(ans)

# 풀이

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')