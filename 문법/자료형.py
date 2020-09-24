# 자료형

# 수 자료형
# round 반올림
# 실수 비교시 사용(실수 정확히 비교 못함)
'''
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

b = round(123.456, 2)
print(b)
'''

# 수 자료형의 연산
# 사칙연산
'''
a = 7
b = 3

# 나누기 -> 실수형으로 처리하므로 주의
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
print(a ** b)
'''

# 리스트 자료형
'''
a = [1, 2, 3, 4, 5]
print(a)

print(a[4])

# 빈 리스트 선언 방법1
a = list()
print(a)

# 빈 리스트 선언 방법2
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 리스트 초기화
n = 10
a = [0] * n
print(a)
'''

# 리스트의 인덱싱과 슬라이싱
# 인덱스값을 이용해 리스트 원소 접근 > 인덱싱
# 음의 정수를 넣으면 원소를 거꾸로 탐색
'''
a = [1, 2, 3, 4, 5, 6, 7]
print(a[-1])
print(a[-3])

a[3] = 7
print(a)

# 연속적인 위치를 갖는 원소들 가져올 때 > 슬라이싱(:)
print(a[1:4])
'''

# 리스트 컴프리헨션
# 리스트 초기화 방법 대괄호안에 조건문과 반복문을 넣는 방식
'''
array = [i for i in range(20) if i % 2 == 1]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
'''
# 언더바(_) 역할
# 반복을 수행하되 반복을 위한 변수의 값을 무시할 때 언더바 사용

# 리스트 관련 기타 메서드
# append() sort() sort(reverse=True)내림차순 reverse() insert(위치, 값) count(값) remove(값)
'''
a = [1, 2, 3, 4]
print("기본 리스트 : ", a)

# 원소 삽입
a.append(2)
print("삽입 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)

# 특정 인덱스에 데이터 추가 > 중간에 원소 삽입 후 위치 조정 시간 초과 주의
a.insert(2, 3)
print("인덱스 2에 3 추가 : ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", a.count(3))

#특정 값 데이터 삭제 > 중간에 원소 제거 후 위치 조정 시간 초과 주의
a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

# 파이썬은 remove_all()과 같은 특정 값 가지는 모든 원소 제거 함수 제공하지 않음
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만 저장
result = [i for i in a if i not in remove_set]
print(result)
'''

# 문자열 자료형

# 문자열 초기화
# "", '' 포함가능 \사용시 큰따옴표나 작은따옴표를 문자열에 원하는 만큼 포함 가능
'''
data = 'hello'
print(data)

data = "Don't you know \"Python\"?"
print(data)
'''

# 문자열 연산
'''
a = "hello"
b = "world"

print(a + " " + b)

a = "String"
print(a * 3)

# 문자열은 내부적으로 리스트와 같이 처리(문자열은 여러 개의 문자가 합쳐진 리스트와 비슷)
a = "ABCDEF"
print(a[2 : 4])
'''

# 튜플 자료형
# 리스트와 비슷하지만 차이가 있다.
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호[], 튜플은 소괄호() 이용
# 그래프 알고리즘, 다익스트라 최단 경로 알고리즘(우선순위 큐) 구현시 사용
'''
a = (1, 2, 3, 4)
print(a)

a[2] = 7 # 변경 안되고 오류
'''

# 사전 자료형
# 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형
# 리스트나 튜플은 값을 순차적으로 저장
'''
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재")

# 사전 자료형 관련 함수
# 키 데이터만 뽑아서 리스트로 이용 > keys()
# 값 데이터만 뽑아서 리스트로 이용 > values()

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
'''

# 집합 자료형
# 집합Set을 처리 기본적으로 리스트 혹은 문자열을 이용해서 만듬
# 중복을 허용하지 않는다.
# 순서가 없다.

# 집합 자료형에서는 키가 존재하지 않고, 값 데이터만 담는다
# set() 함수 를 이용하거나 괄호{} 안에 각 원소를 콤마, 를 기준으로 구분해서 넣는다
'''
# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산
# 합,교,차집합 > |, &, - 이용

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)

# 집합 자료형 관련 함수
# 하나의 집합 데이터에 값을 추가 add() 시간 복잡도 O(1)
# 여러 개의 값을 한꺼번에 추가 update()
# 특정 값을 제거 remove() 시간 복잡도 O(1)

data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
'''