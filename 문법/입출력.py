# 입출력

# 데이터 입력 input() > 한 줄의 문자열을 입력 받는다
# 정수형 데이터로 처리 > int() 함수 사용
# 띄어쓰기로 구분된 여러 개의 정수 자료형 데이터 > list(map(int, input().split()))
# 줄 바꿈 > int(input())
'''
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)
'''
# 공백으로 구분된 데이터 개수가 많지 않다면 > map(int, input().split())
'''
# n, m, k
n, m, k = map(int, input().split())

print(n, m, k)
'''

# 입력을 최대한 빠르게 / 많은 수의 데이터가 연속적을 입력
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수 이용
# input() 함수와 같이 한 줄씩 입력

# rstrip() 함수 > readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거
'''
import sys
data = sys.stdin.readline().rstrip()
print(data)
'''

# 데이터 출력 print() > 변수나 상수를 매개변수로 입력받아 이를 표준 출력
# 각 변수를 콤마, 로 구분, 이 경우 각 변수가 띄어쓰기로 구분되어 출력된다
# 기본적으로 출력 이후에 줄 바꿈을 수행
'''
a = 1
b = 2
print(a, b)
print(a)
print(b)
'''

# 출력할 때 문자열과 수를 함께 출력해야 되는 경우
'''
answer = 7
print("정답은 " + answer + "입니다")
'''
# 위와 같이 사용하면 오류 발생

# str() 함수를 이용하거나 각 자료형을 콤마, 를 기준으로 구분하여 출력
'''
answer = 7
print("정답은 " + str(answer) + "입니다")
print("정답은", str(answer), "입니다")
'''
# 콤마로 구분할 경우 변수의 값 사이에 의도치 않은 공백이 삽입된다

# Python 3.6 이상의 버전부터 f-string 문법을 사용할 수 있다
# 문자열 앞에 접두사 'f'를 붙여 사용, 중괄호{} 안에 변수를 넣어 자료형 변환이 필요 없다
'''
answer = 7
print(f"정답은 {answer}입니다")
'''
