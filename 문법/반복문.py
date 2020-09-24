# 반복문
# 특정한 소스코드를 반복적으로 실행
# while문 for문

# while문
'''
i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)
'''

# for 문
'''
result = 0

for i in range(1, 10):
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격")
'''
# continue 사용시 프로그램의 흐름은 반복문의 처음으로 돌아간다
'''
scores = [90, 85, 77, 65, 97]
black_list = {2, 4}

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격")
'''
# 반복문은 중첩 사용 가능

for i in range(2, 10):
    for j in range(2, 10):
        print(i, "X", j, "=", i * j)
    print()