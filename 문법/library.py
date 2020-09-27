# 주요 라이브러리

# 표준 라이브러리란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
# 파이썬 표준 라이브러리
# https://docs.python.org/ko/3/library/index.html

# 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리
# 순열과 조합 라이브러리를 제공한다

# heapq : 힙(Heap) 기능을 제공하는 라이브러리
# 우선순위 큐 기능을 구현하기 위해 사용

# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리

# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

# math : 필수적인 수학적 기능을 제공하는 라이브러리
# 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함



# 내장 함수
# import 명령어 없이 바로 사용

# sum()
# 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
'''
result = sum([1, 2, 3, 4, 5])
print(result)
'''
# min()
# 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환
# max()
# 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환
'''
result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)
'''

# eval()
# 수학 수식이 문자열 형식으로 들어오면 해당 수직을 계산한 결과를 반환
'''
result = eval("(3 + 5) * 7")
print(result)
print(type(result))
'''

# sorted()
# iterable 객체가 들어왔을 때, 정렬된 결과를 반환
# key 속성으로 정렬 기준을 명시 가능, reverse 속성으로 결과 리스트 뒤질을 수 있다
'''
result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
'''
# 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다
# 정렬 기준은 key 속성 이용
'''
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse= True)
print(result)
'''

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있다
'''
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
'''

# itertools
# 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

# permutations
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
# permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
'''
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
'''
# combinations
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
'''
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
'''

# product
# permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
# 다만 원소를 중복하여 뽑는다
# product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
'''
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)
'''
# combinations_with_replacement
# combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
# 다만 원소를 중복해서 뽑는다
# combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
'''
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)
'''

# heapq
# 파이썬에는 힙(Heap) 기능을 위해 heapq 라이브러리를 제공
# heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현할 때 사용
# PriorityQueue 라이브러리를 사용할 수 있지만, 코딩 테스트 환경에서는 보통 heapq가 더 빠르게 동작
# 파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 
# 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 보통 최초 힙 자료구조의 최상단 원소는 항상 가장 작은 원소이기 때문
# 힙에 원소 삽입 > heapq.heappush() 이용
# 힙에서 원소를 꺼낼 때 > heapq.heappop() 이용
'''
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
'''
# 파이썬은 최대 힙을 제공하지 않는다. 따라서 최대 힙을 구현할 때는 원소의 부호를 임시로 변경하는 방식을 사용
# 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.
'''
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
'''

# bisect
# 파이썬에는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용

# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x): 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 두 함수는 시간 복잡도 O(NlogN)에 동작
'''
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
'''
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때, 효과적으로 사용
# count_by_range(a, left_value, right_value) -> left_value <= x <= right_value
'''
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
'''

# collections
# 유용한 자료구조를 제공하는 표준 라이브러리

# deque, Counter
# 보통 파이썬에서는 deque를 사용해 큐를 구현
# 기본 리스트 자료형은 데이터 삽입, 삭제 등의 다양한 기능을 제공한다. 중간에 특정한 원소를 삽입하는 것도 가능
# 하지만, 리스트 자료형은 append(), pop() 메서드 사용시 '가장 뒤쪽 원소'를 기준으로 수행된다.
# deque에서는 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다. 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에
# 데이터를 삭제할 때는 매우 횩과적으로 사용
# deque는 스택이나 큐의 기능을 모두 포함한다고 볼 수 있기 때문에 대용으로 사용될 수 있다

# deque는 첫 번째 원소를 제거할 때 > popleft()
# 마지막 원소를 제거할 때 > pop()
# 첫 번째 인덱스에 원소 x를 삽입할 때 > appendleft(x)
# 마지막 인덱스에 원소를 삽입할 때 > append(x)

# deque를 큐 자료구조로 이용 > 원소를 삽입 append(), 원소를 삭제 popleft() > 먼저 들어온 원소가 항상 먼저 나가게 된다
'''
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환
'''
# Counter는 등장 횟수를 세는 기능을 제공
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다
'''
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환
'''
# math
# 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
# 팩토리얼, 제곱근, 최대공약수 등을 계산해주는 기능을 포함

# factorial(x) 팩토리얼
'''
import math

print(math.factorial(5))

# sqrt(x) 제곱근

print(math.sqrt(7))

# gcd(a, b) 최대공약수

print(math.gcd(21, 14))

# 상수 필요시

print(math.pi)
print(math.e)
'''
