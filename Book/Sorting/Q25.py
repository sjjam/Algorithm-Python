# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
ans = []
num = len(stages)

rank = []
for i in range(1, n + 1):
    cnt = stages.count(i)
    if num == 0:
        per = 0
    else:
        per = cnt / num
    num -= cnt
    rank.append((i, per))

rank.sort(key=lambda rank: -rank[1])
print(rank)

for i in rank:
    ans.append(i[0])

print(ans)


# 풀이

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        answer.append((i, fail))
        length -= count
    
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer