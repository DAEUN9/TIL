# 방번호
# https://www.acmicpc.net/problem/1475

import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int,list(input())))
li = [0]*10
for n in N:
    if n == 6 or n == 9:
        li[6] += 1
    else:
        li[n] += 1
max_num = 0
for i in range(10):
    if i == 6:
        if max_num < li[i]//2 + li[i]%2:
            max_num = li[i]//2 + li[i]%2
    elif max_num < li[i]:
        max_num = li[i]
# li = [1] * 10
# d = { 6:9, 9:6 }
# cnt = 1
# for n in N:
#     if li[n]:
#         li[n] = 0
#     elif n==6 or n==9:
#         if li[d[n]]:
#             li[d[n]] = 0
#         else:
#             cnt += 1
#             li = [1] * 10
#             li[n] = 0
#     else:
#         li = [1]*10
#         li[n] = 0
#         cnt += 1
print(max_num)