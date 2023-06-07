def solution(n, money):
    dp = [1] + [0]*n
    for m in sorted(money):
        for i in range(1, n+1):
            if i>=m:
                dp[i] += dp[i-m]
    return dp[n]%1000000007