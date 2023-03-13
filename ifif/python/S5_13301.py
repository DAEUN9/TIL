N = int(input())
dp = [0]*(N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-2]+dp[i-1]
if N==1:
    print(4)
elif N==2:
    print(6)
else:
    print(dp[N]*3 + dp[N-1]*2 + dp[N-2]*2 + dp[N-3])