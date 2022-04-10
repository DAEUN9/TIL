# 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070

import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def pipe_move(r, c, p):
    global cnt
    # q = deque([(0, 1, 0)])
    if r == N-1 and c == N-1:
        cnt += 1
        return
    if r + 1 < N and c+1 < N and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r][c+1]==0:
        pipe_move(r + 1, c + 1, 2)
    if p == 0:
        if c+1<N and arr[r][c+1] == 0:
            pipe_move(r, c+1, 0)
    elif p == 1:
        if r+1<N and arr[r+1][c] == 0:
            pipe_move(r+1, c, 1)
    else:
        if r+1<N and arr[r+1][c] == 0:
            pipe_move(r+1, c, 1)
        if c+1<N and arr[r][c+1] == 0:
            pipe_move(r, c+1, 0)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
pipe_move(0, 1, 0)
print(cnt)
