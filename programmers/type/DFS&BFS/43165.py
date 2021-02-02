# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

from itertools import combinations

def solution(numbers, target):
    answer = 0
    all_s = sum(numbers)
    for i in range(1, len(numbers) + 1):
        for j in list(combinations(numbers, i)):
            tmp = sum(j)
            if all_s - tmp - tmp == target:
                answer += 1

    return answer

# dfs 풀이
# https://itholic.github.io/kata-target-number/ 그림 참고

def dfs(nums, i, n, t):
    ret = 0
    print(i, n)
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

solution([1, 1, 1, 1, 1], 3)