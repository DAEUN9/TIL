# 부분합
# https://www.acmicpc.net/problem/1806

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def find(n, s):
    i = 0
    while i < n:
        i += 1
        for j in range(n+1):
            if j+i>n:
                break
            if li[j+i] - li[j] >= s:
                return i
    return 0

N, S = map(int, input().split())

li = [0] + list(map(int, input().split()))
for i in range(N):
    li[i+1] += li[i]

print(find(N, S))
