# 샤워실 바닥 깔기 (Small)
# r1 x
# https://www.acmicpc.net/problem/14600

# https://rebro.kr/64
# https://welog.tistory.com/232

# 2**n X 2**n 크기의 정사각형에 1x1 한 칸을 제외하고 항상 L-트로미노로 모두 채울 수 있다.

def check(size, a, b):
    for i in range(a, a + size):
        for j in range(b, b + size):
            if data[i][j] != 0:
                return False
    return True

def solution(size, a, b):
    global num
    num += 1
    # 정사각형을 4사분면으로 나누어 check
    s = size // 2
    # 2
    if check(s, a, b):
        data[a + s - 1][b + s - 1] = num
    # 1
    if check(s, a, b + s):
        data[a + s - 1][b + s] = num
    # 3
    if check(s, a + s, b):
        data[a + s][b + s - 1] = num
    # 4
    if check(s, a + s, b + s):
        data[a + s][b + s] = num
    
    if size == 2:
        return
    solution(s, a, b) # 2
    solution(s, a, b + s) # 1
    solution(s, a + s, b) # 3
    solution(s, a + s, b + s) # 4

k = int(input())
y, x = map(int, input().split())
data = [[0] * 2**k for _ in range(2**k)]
data[2**k - x][y - 1] = -1
num = 0
solution(2**k, 0, 0)
for i in range(2**k):
    for j in range(2**k):
        print(data[i][j], end=' ')
    print()