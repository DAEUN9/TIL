import sys
sys.stdin = open("input.txt", "r")
N, M, K = map(int, input().split())

max_team = min(N//2, M)
while True:
    a = N - max_team*2
    b = M - max_team
    if a+b >= K:
        break
    else:
        max_team -= 1
print(max_team)