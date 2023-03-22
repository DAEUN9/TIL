import sys
sys.stdin = open("input.txt", "r")
n = int(input())
A = list(map(int, input().split()))
A.sort()
total = sum(A)
answer = 0
for a in A:
    answer += a*(total-a)
    total-=a
print(answer)