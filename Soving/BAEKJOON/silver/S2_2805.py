# 나무자르기
# https://www.acmicpc.net/problem/2805

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

big_tree = max(li)

start = 1
end = big_tree
middle = 0
# while start<=end:
#     middle = (start+end)//2
#     length = 0
#     for l in li:
#         if l>middle:
#             length += l-middle
#         if length >M:
#             break
#     if length < M:
#         end = middle-1
#     else:
#         start = middle+1
# print(end)


def binary_search(s, e, target):
    global middle
    if s>e:
        return
    m = (s+e)//2
    length = 0
    for l in li:
        if l>m:
            length += l-m
        if length>target:
            break
    if target <= length:
        if m > middle:
            middle = m
    if length < target:
        binary_search(s, m-1, target)
    else:
        binary_search(m+1, e, target)

binary_search(start, end, M)
print(middle)