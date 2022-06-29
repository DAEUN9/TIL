# 보물
# https://www.acmicpc.net/problem/1026

import sys

sys.stdin = open('input.txt','r')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sort_B = sorted(B)
sort_A = sorted(A, reverse=True)

total = 0
for i in range(N):
    total += sort_B[i]*sort_A[i]

print(total)