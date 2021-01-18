# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884
# X

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    checked = [0] * len(routes)

    for i in range(len(routes)):
        if checked[i] == 0:
            cam = routes[i][1]
            answer += 1
        for j in range(i + 1, len(routes)):
            if checked[j] == 0 and cam >= routes[j][0] and cam <= routes[j][1]:
                checked[j] = 1

    return answer

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    print(routes)
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])