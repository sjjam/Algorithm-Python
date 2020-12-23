# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

# 효율성 3개 실패

# def solution(words, queries):
#     answer = []

#     for q in queries:
#         idx = q.index("?")
#         t = ''
#         r = 0
#         c = 0
#         if idx != 0:
#             t = q[:idx]
#             r = len(q) - len(t)
#         else:
#             r = q.count("?")
#             t = q[r:]
#             c = 1
#         length = len(t)
#         cnt = 0
#         for w in words:
#             if c == 0:
#                 if t == w[:length] and len(w[length:]) == r:
#                     cnt += 1
#             else:
#                 if t == w[r:] and len(w[:r]) == r:
#                     cnt += 1
#         answer.append(cnt)
#     return answer

# solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])



# 풀이

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?':
            print(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            print(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer