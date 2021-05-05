# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    now = 0

    while q:
        answer += 1
        now -= q.pop(0)
        if len(truck_weights) > 0:
            if now + truck_weights[0] <= weight:
                now += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return answer