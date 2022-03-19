# 학생 수
N = int(input())

students = []
for n in range(N):
    stu = input().split()
    students.append([stu[0], int(stu[1])])
# 람다 키 이용하기
# key = lambda 변수명: 기준
answer = sorted(students, key = lambda students: students[1])
for a in answer:
    print(a[0], end=' ')