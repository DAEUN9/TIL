N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[0][0] = 0
for t in range(1, 10):
    dp[0][t] = 1

for i in range(1, N+1):
    for j in range(10):
        for k in [j-1, j+1]:
            if 0 <= k < 10:
                dp[i][j] += dp[i-1][k]
print(sum(dp[N-1])%1000000000)