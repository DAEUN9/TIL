import sys
sys.stdin = open("input_dt.txt", "r")
T = int(input())
k = int(input())
dp = [0]*(T+1)
for _ in range(k):
    P, N = map(int, input().split())
    temp = dp[:]
    for n in range(1, N+1):
        if P*n <= T:
            dp[P*n] += 1
            for j in range(P * n + 1, T + 1):
                dp[j] += temp[j - P * n]
print(dp[-1])


