import sys
sys.stdin = open("input.txt", "r")
R, C, W = map(int, input().split())
dp = [[1]]
for i in range(1, R+W):
    temp = [1]
    for j in range(1, i):
        temp.append(dp[i-1][j-1] + dp[i-1][j])
    temp.append(1)
    dp.append(temp)
answer = 0
cnt = 0
for r in range(R-1, R+W-1):
    cnt += 1
    # print(dp[r])
    # print(dp[r][C-1:C+cnt-1])
    answer += sum(dp[r][C-1:C+cnt-1])
print(answer)