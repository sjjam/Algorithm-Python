# 국영수

n = int(input())
student = []

for i in range(n):
    line = input().split()
    student.append((line[0], int(line[1]), int(line[2]), int(line[3])))

student.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for i in range(n):
    print(student[i][0])


# 풀이

n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])