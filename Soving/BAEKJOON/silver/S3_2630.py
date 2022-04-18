# 색종이 만들기
# https://www.acmicpc.net/problem/2630

import sys
sys.stdin = open('input.txt','r')
def div(s, e, n):
    global cnt_blue, cnt_white
    gijun = arr[s][e]
    flag = True
    for i in range(s, s+n):
        for j in range(e, e+n):
            if gijun != arr[i][j]:
                flag = False
    if flag:
        if gijun == '1':
            cnt_blue += 1
        else:
            cnt_white += 1
        return
    else:
        div(s, e, n//2)
        div(s, e+n//2, n//2)
        div(s+n//2, e, n//2)
        div(s+n//2, e+n//2, n//2)
N = int(input())
arr = list(list(input().split()) for _ in range(N))
cnt_white = 0
cnt_blue = 0
div(0, 0, N)
print(cnt_white)
print(cnt_blue)