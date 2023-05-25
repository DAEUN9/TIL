import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
numbers = [float(input()) for _ in range(N)]
dp = [numbers[0]]
for i in range(1, N):
    dp.append(max(dp[i-1]*numbers[i], numbers[i]))
print('%.3f' % max(dp))