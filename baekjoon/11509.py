# 풍선 맞추기
# r1 x
# https://www.acmicpc.net/problem/11509

# https://javaiyagi.tistory.com/599
# https://baactree.tistory.com/3

n = int(input())
h = list(map(int, input().split()))
ans = 0
flag = [0] * 1000001

for i in range(n):
    if flag[h[i]] == 0:
        ans += 1
    else:
        flag[h[i]] -= 1
    flag[h[i] - 1] += 1
    
print(ans)