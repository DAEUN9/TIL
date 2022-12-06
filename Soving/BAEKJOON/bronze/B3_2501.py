# 약수구하기
# https://www.acmicpc.net/problem/2501

import sys
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if(N%i == 0):
        cnt += 1
    if(cnt==K):
        print(i)
        break
else:
    print(0)