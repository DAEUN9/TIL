# 신입 사원
#
# 그리디 알고리즘
# 정렬

import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks.sort()
    cnt = 1
    max_m = ranks[0][1]

    for s, m in ranks[1:]:
        if m < max_m:
            cnt +=1
            max_m = m
    print(cnt)