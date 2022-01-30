# 단어 맞추기
# r1 x
# https://www.acmicpc.net/problem/9081

# https://hillier.tistory.com/102

import sys

def nextPermutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return False
 
    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result

input = sys.stdin.readline
for _ in range(int(input())):
    word = list(input().rstrip())
    ans = nextPermutation(word)
    
    if not ans:
        print(''.join(word))
    else:
        print(''.join(ans))