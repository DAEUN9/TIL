# N-Queen
# https://www.acmicpc.net/problem/9663

import sys

N = int(sys.stdin.readline())

def promising(i):
    k = 0
    flag = True
    while k <i:
        if (cols[i] == cols[k]) or (abs(cols[i]-cols[k]) == (i-k)):
            return False
        k += 1
    return flag

def queen(i):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            cols[i] = j
            if (promising(i)):
                queen(i+1)

cols = [0] * N
cnt = 0
queen(0)
print(cnt)