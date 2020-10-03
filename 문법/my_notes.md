# 정리

### 실수 입력받아 원하는 소수점까지 출력

a = float(input())

print('%.2f' % a)



### print() 속성 'sep=' 사용시 출력값 사이에 특정 문자 넣어 구분 가능

print(5, 9, sep=":")



### 원하는 길이만큼 출력(공백 0으로 채움)

y, m, d = map(int, input().split("."))

print('%04d' %y, '%02d' %m, '%02d' %d, sep=".")



### 2, 8, 16 진수

#### format 이용

a = format(int(input()), 'o') # 'b' 'o' 'x'

print(a)



#### print로 바로 출력

a = int(input())

print('%x' %a) # '%X' 대문자 사용시 대문자로 출력



#### 입력받은 진수와 다른 진수로 출력

a = input()

n = int(a,16) # a를 16진수로 반꾼 값을 10진수로 변경해서 저장

print("%o" % n) # n을 8진수로 출력



### ord() 문자의 아스키 코드 값을 반환(영문자 -> 아스키 10진수)

a = input()

n = ord(a)

print(n)



### 10진수 -> 아스키 문자

a = input()

n = int(a)

c = chr(n)

print(c)



### 배열을 정렬한 후 조합을 실행하면 결과도 정렬이 된 상태로 나온다



### 2차원 배열에 값 입력 받기

a = [[0]*19 for i in range(19)]

for i in range(19):
    x = list(map(int, input().split()))
    for j in range(19):
        a[i][j] = x[j]