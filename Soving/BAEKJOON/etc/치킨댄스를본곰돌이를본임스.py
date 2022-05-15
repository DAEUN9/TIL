N = int(input())
A, B = map(int, input().split())

answer = min(N, B)
N -= answer
if N:
    answer += min(N, A//2)

print(answer)