# 조건문
# 프로그램의 흐름을 제어
'''
x = 15

if x>= 10:
    print(x)

score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else:
    print("학점: F")

# 코드의 블록(Block)을 들여쓰기로 설정, 들여쓰기가 같은 부분은 함께 실행
score = 95

if score >= 70:
    print('성적이 70점 이상')
    if score >= 90:
        print('우수')
else:
    print('성적이 70점 미만')
    print('분발')

print('프로그램 종료')
'''

# 파이썬에서 들여쓰기는 스페이스 바 4번 입력

# 비교 연산자
# x == y / x != y / x > y / x < y / x >= y / x <= y

# 논리 연산자
# x and y : x, y 모두 참일 때 참
# x or y : x, y 중 하나만 참이어도 참
# not x : x가 거짓일 때 참

# 파이썬의 기타 연산자
# in, not in 연산자 : 자료형 안에 어떠한 값이 존재하는지 확인
# x in 리스트
# x not in 문자열

# 조건문 값이 참일 때, 아무것도 처리하고 싶지 않으면 pass 이용
'''
score = 85

if score >= 80:
    pass
else:
    print('80 미만')

print('프로그램 종료')

# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈 하지 않아도 된다

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result)

# 조건부 표현식 이용

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들 때 매우 편리

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 위와 같은 코드가 더 간결해짐
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)
'''
# 파이썬은 0 < x < 20과 같이 부등식 사용 가능