# 함수
# 동일한 알고리즘을 반복적으로 수행할 때 효과적
'''
def 함수명(매개변수):
    실행할 소스코드
    return 반환값

def add(a, b):
    return a + b

print(add(3, 7))

def add(a, b):
    print('함수의 결과:', a + b)

add(3, 7)
'''
# 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다.
# 매개변수 a, b가 사용될 때, 함수를 호출하는 라인에서 인자 a, b를 지칭해서 각각 값을 넣을 수 있다.
'''
def add(a, b):
    print('함수의 결과:', a + b)

add(b = 3, a = 7)
'''
# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우
# global 키워드 이용 > 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
'''
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)
'''
# 람다 표현식 사용 가능 > 함수를 간단하게 작성하여 적용
# 함수를 한 줄에 작성
'''
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현
print((lambda a, b: a + b)(3, 7))
'''