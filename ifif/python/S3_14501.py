import sys
sys.stdin = open("input.txt", "r")
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)
for n in range(N):
    t, p = schedules[n]
    if n+t<=N:
        dp[n+t] = max(dp[n] + p, dp[n+t])
print(dp)