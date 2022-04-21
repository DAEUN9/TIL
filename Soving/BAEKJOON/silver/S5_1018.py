import sys
sys.stdin = open('input.txt','r')

def check(r, c, flag):
    global min_cnt
    cnt = 0
    for i in range(r, r+8):
        idx = 0
        while idx < 8:
            if arr[i][c+idx] != search[flag][idx]:
                cnt += 1
            idx += 1
        flag = (flag+1)%2
    if cnt < min_cnt:
        min_cnt = cnt
    return

N, M = map(int,input().split())
arr = [input() for _ in range(N)]
min_cnt = int(1e9)
search = ['WBWBWBWB', 'BWBWBWBW']
for r in range(N-7):
    for c in range(M-7):
        check(r, c, 0)
        check(r, c, 1)
print(min_cnt)