# 스티커 모으기(2)
# r1 x
# https://programmers.co.kr/learn/courses/30/lessons/12971


# https://inspirit941.tistory.com/158


def solution(sticker):
    answer = 0
    
    if len(sticker) == 1:
        return sticker[0]
    
    dp = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]
    dp[1] = dp[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    answer = max(max(dp), max(dp2))

    return answer