# 로또
# https://www.acmicpc.net/problem/6603

import sys

sys.stdin = open('input.txt', 'r')

def dfs(l, n):
    if len(l) == 6:
        answer.append(l)
        return
    for i in range(n+1, k):
        dfs(l+[li[i]], i)

while True:
    li = list(map(int, input().split()))
    k = li[0]
    if k == 0:
        break
    li = li[1:]
    li.sort()
    answer = []
    dfs([], -1)
    for a in answer:
        print(*a)
    print()

