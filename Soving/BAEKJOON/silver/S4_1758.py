import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
answer = 0
grades = [int(input()) for _ in range(N)]
grades.sort(reverse=True)
for n in range(N):
    grade = grades[n]
    if grade - (n) > 0:
        answer += grade - n
print(answer)