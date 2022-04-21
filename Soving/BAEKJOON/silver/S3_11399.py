# ATM
# https://www.acmicpc.net/problem/11399

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
li = list(map(int, input().split()))
li.sort()
total = li[0]
answer = li[0]
for i in range(1, N):
    total = total + li[i]
    answer += total
print(answer)