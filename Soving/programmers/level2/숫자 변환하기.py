def solution(x, y, n):
    dp = [1e9] * (y+1)
    dp[x] = 0
    for i in range(x, y+1):
        curr = dp[i]
        if i+n < y+1:
            dp[i+n] = min(curr +1, dp[i+n])
        if i*2 < y+1:
            dp[i*2] = min(curr + 1, dp[i*2])
        if i*3 < y+1:
            dp[i*3] = min(curr + 1, dp[i*3])
    if dp[-1] == 1e9:
        return -1
    return dp[-1]