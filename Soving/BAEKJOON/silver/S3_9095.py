# 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

import sys

sys.stdin =open('input.txt','r')


def hap(n, total):
    global cnt
    if n < total:
        return
    if n == total:
        cnt += 1
        return
    for i in range(1, 4):
        hap(n, total + i)

T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    hap(N, 0)
    print(cnt)