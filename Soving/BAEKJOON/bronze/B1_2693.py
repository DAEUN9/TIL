# N번째 큰 수
# https://www.acmicpc.net/problem/2693

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    l = list(map(int, input().split()))
    l.sort()
    print(l[-3])