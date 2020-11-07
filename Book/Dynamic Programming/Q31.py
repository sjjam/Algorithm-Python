# 금광

t = int(input())
for i in range(t):
    n, m = map(int, input().split())    
    x = list(map(int, input().split()))
    arr = []
    idx = 0
    for j in range(n):
        arr.append(x[idx:idx + m])
        idx += m
    
    d = [0] * (m + 1)
    for j in range(n):
        d[1] = max(d[1], arr[j][0])