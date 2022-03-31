# 부분수열의 합
# https://www.acmicpc.net/problem/14225

import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, n):
    if i == N:
        if n:
            subset.add(n)
        return
    dfs(i+1, n)
    dfs(i+1, n+li[i])

N = int(input())
li = list(map(int, input().split()))
subset = set()
dfs(0, 0)
subset = sorted(list(subset))
answer = 0
for i in range(1, subset[-1]+1):
    if subset[i-1] == i:
        continue
    answer = i
    break
else:
    answer = subset[-1]+1
print(answer)