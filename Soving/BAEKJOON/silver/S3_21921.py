# 블로그
# https://www.acmicpc.net/problem/21921

import sys
sys.stdin = open('input.txt', 'r')

# X일동안 가장 많이 들어온 방문자수
N, X = map(int,input().split())

li = list(map(int, input().split()))
max_val = 0
cnt = 0
dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + li[i-1]
for i in range(N-X+1):
    curr = dp[i+X] - dp[i]
    if curr > max_val:
        max_val = curr
        cnt = 1
    elif curr == max_val:
        cnt += 1
if max_val:
    print(max_val)
    print(cnt)
else:
    print('SAD')