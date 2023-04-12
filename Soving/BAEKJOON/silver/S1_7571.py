import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def positive(n):
    if n>=0:
        return n
    else: return -n

N, M = map(int ,input().split())

points = []
for _ in range(M):
    points.append(list(map(int, input().split())))
answer = 1e9
for i in range(1, N+1):
    for j in range(1, N+1):
        temp = 0
        for x, y in points:
            temp += positive(x-i)+positive(y-j)
        answer = min(temp, answer)
print(answer)