# 통신병 민코씨
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AX_PlrcKe_YDFARi

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    # 가로크기 x, 세로크기 y
    X, Y = map(int,input().split())
    arr = [list(input()) for _ in range(Y)]
    visited = [[0]*X for _ in range(Y)]
    for i in range(X):
        for j in range(Y):
            if arr[i][j] =