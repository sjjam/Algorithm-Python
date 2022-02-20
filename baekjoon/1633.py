# 최고의 팀 만들기
# r1 x
# https://www.acmicpc.net/problem/1633

# https://velog.io/@kjihye0340/%EB%B0%B1%EC%A4%80-1633%EC%B5%9C%EA%B3%A0%EC%9D%98-%ED%8C%80-%EB%A7%8C%EB%93%A4%EA%B8%B0

import sys

def solution(i, widx, bidx, n):
    if widx == 15 and bidx == 15:
        return 0
    if i == n:
        return 0

    if dp[i][widx][bidx] != 0:
        return dp[i][widx][bidx]

    ans = solution(i + 1, widx, bidx, n)

    if widx < 15:
        ans = max(ans, solution(i + 1, widx + 1, bidx, n) + white[i])

    if bidx < 15:
        ans = max(ans, solution(i + 1, widx, bidx + 1, n) + black[i])

    dp[i][widx][bidx] = ans
    return dp[i][widx][bidx]

input = sys.stdin.readline
white = [0] * 1001
black = [0] * 1001
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(1001)]

idx = 0
while True:
    line = input()
    if not line:
        break

    w, b = map(int, line.split())
    white[idx] = w
    black[idx] = b

    idx += 1

print(solution(0, 0, 0, idx))