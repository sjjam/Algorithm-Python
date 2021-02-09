# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
# r1 x

def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top])==0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    answer.reverse()
    return answer

print(solution([['ICN','BBB'],['BBB','ICN'],['ICN','AAA'],['AAA','DDD'],['DDD','AAA']]))