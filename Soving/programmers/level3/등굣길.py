def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][1], dp[1][0] = 1, 1
    for y, x in puddles:
        dp[x-1][y-1] = -1
    for i in range(n):
        for j in range(m):
            if dp[i][j] < 0:
                continue
            if 0<=i-1<n and dp[i-1][j] > 0:
                dp[i][j] += dp[i-1][j]
            if 0<=j-1<m and dp[i][j-1] > 0:
                dp[i][j] += dp[i][j-1]
    
    return dp[-1][-1]%1000000007
